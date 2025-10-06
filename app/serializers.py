from rest_framework import serializers
from .models import *

class UserSerializers(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RegisterSerializers(serializers.Serializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','password', 'confirm_password']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "passwords are not matched"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
class NotesSerializer(serializers.Serializer):

    class Meta:
        model = Notes
        fields = ['user', 'created_on', 'updated_on']