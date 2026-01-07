from django.contrib import admin
from .models import Register, Video, Movie, TvShow, MyList

admin.site.register({Register})
admin.site.register({Video})
admin.site.register({Movie})
admin.site.register({TvShow})
admin.site.register({MyList})