"""
URL configuration for video project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from videoapp.views import RegisterView, PopularMovieView, PopularTvshowView, VideoView, ActionView, DramaView, ComedyView, HorrorView, RomanceView, ScifiView, DocumentaryView, ThrillerView

router = routers.DefaultRouter()
router.register('registers', RegisterView, 'register')
router.register('popularmovies', PopularMovieView, 'popularmovie')
router.register('populartvshows', PopularTvshowView, 'populartvshow')
router.register('videos', VideoView, 'video')
router.register('actions', ActionView, 'action')
router.register('dramas', DramaView, 'drama')
router.register('comedy', ComedyView, 'comedy')
router.register('horrors', HorrorView, 'horror')
router.register('romance', RomanceView, 'romance')
router.register('scifi', ScifiView, 'scifi')
router.register('documentary', DocumentaryView, 'documentary')
router.register('thrillers', ThrillerView, 'thriller')
router.register('mylists', ThrillerView, 'mylist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
