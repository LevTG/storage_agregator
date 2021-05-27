from rest_framework import serializers

from .models import Profile


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Profile
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)
