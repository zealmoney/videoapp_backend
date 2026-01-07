from django.db import models

GENRES = [
    ('act', 'Action'),
    ('drm', 'Drama'),
    ('cmd', 'Comedy'),
    ('hor', 'Horror'),
    ('rom', 'Romance'),
    ('sci', 'Sci-fi'),
    ('doc', 'Documentary'),
    ('thr', 'Thrillers'),
    ('pop', 'popular Tv Shows'),
    ('mov', 'popular Movies'),
    ('wall', 'Wallpapers')
]

class Register(models.Model): 
    firstname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, choices=GENRES)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, choices=GENRES)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")

    def __str__(self):
        return self.title

class TvShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, choices=GENRES)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")

    def __str__(self):
        return self.title

class MyList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")
    email = models.TextField()

    def __str__(self):
        return self.title