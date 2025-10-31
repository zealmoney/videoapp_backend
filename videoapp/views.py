from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, Video, MyList, Wallpaper
from .serializers import RegisterSerializer, VideoSerializer, MyListSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ActionView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='act').values()
    serializer_class = VideoSerializer

class DramaView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='drm').values()
    serializer_class = VideoSerializer

class ComedyView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='cmd').values()
    serializer_class = VideoSerializer

class HorrorView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='hor').values()
    serializer_class = VideoSerializer

class RomanceView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='rom').values()
    serializer_class = VideoSerializer

class ScifiView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='sci').values()
    serializer_class = VideoSerializer

class DocumentaryView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='doc').values()
    serializer_class = VideoSerializer

class ThrillerView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='thr').values()
    serializer_class = VideoSerializer

class PopularMovieView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='mov').values()
    serializer_class = VideoSerializer

class PopularTvshowView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='pop').values()
    serializer_class = VideoSerializer

class MyListView(viewsets.ModelViewSet):
    queryset = MyList.objects.all()
    serializer_class = MyListSerializer

class WallpaperView(viewsets.ModelViewSet):
    queryset = Video.objects.filter(description='wall').values()
    serializer_class = VideoSerializer

