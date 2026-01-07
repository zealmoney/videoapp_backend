from rest_framework import serializers
from .models import Register, Video, Movie, TvShow, MyList

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Register

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Video

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie

class TvShowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TvShow

class MyListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MyList