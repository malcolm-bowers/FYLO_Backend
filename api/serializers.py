from rest_framework import serializers
from app.models import Base, File
from accounts.models import CustomUser

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class BaseSerializer(serializers.ModelSerializer):
    files = FileSerializer(source='file_set', many=True)
    class Meta:
        model = Base
        fields = ('id', 'name', 'location', 'files')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user