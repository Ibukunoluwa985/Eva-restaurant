from django.contrib import admin
from .models import Menu, DeliveryLocation, Reservation

# menu registering, filter
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "plate", "recipies", "cost", "dish_type", "added_on")
    # menu filter
    list_filter = ("dish_type","added_on", "cost", "recipies",)
    # menu search
    search_fields = ("id__startswith","dish_type__startswith","plate__startswith", "recipies__startswith", "added_on__startswith", )

# menu registering, filter
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "number_of_person", "phone_number", "email")
    # menu filter
    list_filter = ("full_name","number_of_person", "phone_number", "email",)
    # menu search
    search_fields = ("id__startswith","full_name__startswith","number_of_person__startswith", "phone_number__startswith", "email__startswith", )

# menu registering, filter
@admin.register(DeliveryLocation)
class DeliveryLocationAdmin(admin.ModelAdmin):
    list_display = ("id", "ordering_plate","phone_number","number_of_plate", "delivery_location")
    # menu filter
    list_filter = ("number_of_plate","delivery_location",)
    # menu search
    search_fields = ("id__startswith","ordering_plate__startswith","phone_number__startswith","number_of_plate__startswith","delivery_location__startswith", )