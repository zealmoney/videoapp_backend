from rest_framework import serializers
from .models import Register, Video, Movie, TvShow, MyList, VideoLike

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Register

class VideoSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'image',
            'videoUrl',
            'details',
            'likes_count',
            'is_liked',
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if not request:
            return False

        email = None

        if hasattr(request, 'query_params'):
            email = request.query_params.get('email')

        if not email and hasattr(request, 'data'):
            email = request.data.get('email')

        if not email:
            return False

        return VideoLike.objects.filter(video=obj, email=email).exists()

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