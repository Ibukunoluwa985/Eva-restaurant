from django.contrib import admin
from .models import Menu, DeliveryLocation

# menu registering, filter
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("plate", "recipies", "cost", "dish_type", "added_on")
    # menu filter
    list_filter = ("dish_type","added_on", "cost", "recipies",)
    # menu search
    search_fields = ("dish_type__startwith","plate__startswith", "recipies__startswith", "added__startswith", )


# menu registering, filter
@admin.register(DeliveryLocation)
class DeliveryLocationAdmin(admin.ModelAdmin):
    list_display = ("number_of_plate", "delivery_location")
    # menu filter
    list_filter = ("number_of_plate","delivery_location",)
    # menu search
    search_fields = ("number_of_plate__startwith","delivery_location__startswith", )