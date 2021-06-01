from rest_framework import serializers
from django.contrib.auth import get_user_model

Profile = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
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
            "password"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]

        password = validated_data["password"]
        if (email and Profile.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        user = Profile(username=username)
        user.set_password(password)
        user.save()
        return user
