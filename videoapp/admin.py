from django.contrib import admin
from .models import Register, Video, MyList, Wallpaper

admin.site.register({Register})
admin.site.register({Video})
admin.site.register({MyList})
admin.site.register({Wallpaper})