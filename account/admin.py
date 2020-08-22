from django.contrib import admin
from .models import ProfileImage

# Register your models here.

# profile image registering
@admin.register(ProfileImage)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("id", "profile_img")