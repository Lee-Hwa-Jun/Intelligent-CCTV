from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    admin.site.register(User)
    admin.site.register(File_list)