from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework_jwt.settings import api_settings

from company.serializers import CompanySerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

Profile = get_user_model()


class ProfileRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True},
                        'first_name': {'required': False},
                        'last_name': {'required': False},
        }

    def create(self, profile_data):
        username = profile_data["username"]
        email = profile_data["email"]
        password = profile_data["password"]
        if email and Profile.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError(
                {"username": "Username must be unique."})
        user = Profile.objects.create_user(**profile_data)
        user.set_password(password)
        user.save()

        # serializer = ProfileLoginSerializer(data={'username': user.username, 'password': password})
        # serializer.is_valid(raise_exception=True)
        # return serializer.data
        return user


class ProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", )
        password = data.get("password", )
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        try:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            update_last_login(None, user)
        except Profile.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }


class ProfileSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(source='company_set', many=True)
    lookup_field = 'username'

    class Meta:
        model = Profile
        fields = [
            'id',
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            'companies'
        ]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    lookup_field = 'username'

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if Profile.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if Profile.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.username != instance.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data.get('first_name', )
        instance.last_name = validated_data.get('last_name', )
        instance.email = validated_data.get('email', )
        instance.username = validated_data.get('username', )

        instance.save()

        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)
    lookup_field = 'username'

    class Meta:
        model = Profile
        fields = ('old_password', 'password')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return ProfileSerializer(instance).data
