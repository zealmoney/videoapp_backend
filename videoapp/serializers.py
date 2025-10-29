from rest_framework import serializers
from .models import Register, Video, MyList, Wallpaper

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Register

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Video

class MyListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MyList

class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Wallpaper