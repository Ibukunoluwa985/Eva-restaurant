from django.contrib import admin
from .models import Chef

# Register your models here.

# chef registering, filter
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "joined_on",)
    # chef filter
    list_filter = ("joined_on", "name", "role",)
    # chef search
    search_fields = ("id__startswith", "name__startswith", "role__startswith", "joined_on__startswith", )