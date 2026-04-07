from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Register, Video, Movie, TvShow, MyList, VideoLike
from .serializers import RegisterSerializer, VideoSerializer, MovieSerializer, TvShowSerializer, MyListSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TvShowView(viewsets.ModelViewSet):
    queryset = TvShow.objects.all()
    serializer_class = TvShowSerializer


class ActionView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='act')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DramaView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='drm')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ComedyView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='cmd')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class HorrorView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='hor')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class RomanceView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='rom')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ScifiView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='sci')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DocumentaryView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='doc')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ThrillerView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='thr')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowActionView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='act_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowDramaView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='drm_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowComedyView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='cmd_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowHorrorView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='hor_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowRomanceView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='rom_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowScifiView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='sci_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowDocumentaryView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='doc_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TvShowThrillerView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='thr_tvshow')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PopularMovieView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='mov')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PopularTvshowView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='pop')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class MyListView(viewsets.ModelViewSet):
    queryset = MyList.objects.all()
    serializer_class = MyListSerializer


class WallpaperView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='wall')
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ToggleVideoLikeView(APIView):
    def post(self, request, video_id):
        email = request.data.get('email')

        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        video = get_object_or_404(Video, id=video_id)

        existing_like = VideoLike.objects.filter(video=video, email=email).first()

        if existing_like:
            existing_like.delete()
            return Response({
                'liked': False,
                'likes_count': video.likes.count()
            }, status=status.HTTP_200_OK)

        VideoLike.objects.create(video=video, email=email)

        return Response({
            'liked': True,
            'likes_count': video.likes.count()
        }, status=status.HTTP_200_OK)