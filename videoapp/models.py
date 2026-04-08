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
    ('wall', 'Wallpapers'),
    ('act_tvshow', 'Action_TvShows'),
    ('drm_tvshow', 'Drama_TvShows'),
    ('cmd_tvshow', 'Comedy_TvShows'),
    ('hor_tvshow', 'Horror_TvShows'),
    ('rom_tvshow', 'Romance_TvShows'),
    ('sci_tvshow', 'Sci-fi_TvShows'),
    ('doc_tvshow', 'Documentary_TvShows'),
    ('thr_tvshow', 'Thrillers_TvShows'),
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
    count_likes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, choices=GENRES)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")
    count_likes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class TvShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, choices=GENRES)
    image = models.TextField()
    videoUrl = models.TextField()
    details = models.TextField(default="")
    count_likes = models.IntegerField(default=0, blank=True)

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

class VideoLike(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'email')

    def __str__(self):
        return f"{self.email} liked {self.video.title}"