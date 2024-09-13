from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'phone_number')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        # Send activation email logic here
        return user
