from django.contrib import admin
from .models import userInfo

# Register your models here.

class userdata(admin.ModelAdmin):
    list_display=['name','email','city','mobile']

admin.site.register(userInfo,userdata)
