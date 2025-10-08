from rest_framework import serializers
from .models import Register, Video

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Register

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Video