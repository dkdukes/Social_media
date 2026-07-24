from django.contrib import admin
from . models import CustomUser,Tags,Posts,Comments,Likes,Followers,Notifications

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Tags)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Followers)
admin.site.register(Notifications)