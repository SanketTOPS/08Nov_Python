from django.contrib import admin
from .models import usersignup

# Register your models here.
class signupAdmin(admin.ModelAdmin):
    list_display=['id','firstname','lastname','email','dob','mobile','address']

admin.site.register(usersignup,signupAdmin)
