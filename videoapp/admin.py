from django.contrib import admin
from .models import Register, Video, MyList

admin.site.register({Register})
admin.site.register({Video})
admin.site.register({MyList})