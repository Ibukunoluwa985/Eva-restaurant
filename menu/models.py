# importing required tools
from django.db import models

# Create your models here.

# menu model
class Menu(models.Model):
    plate = models.CharField(max_length=50, default=None, null=True)
    plate_info = models.TextField(max_length=2000, default=None, null=True)
    plate_img = models.ImageField(upload_to='plate_img', default=None)
    recipies = models.CharField(max_length=50, default=None, null=True)
    dish_type = models.CharField(max_length=50, default=None, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()

# reservation model
class Reservation(models.Model):
    full_name = models.TextField(max_length=100, default=None, null=True)
    number_of_person = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100, default=None, null=True)

# delivery model
class DeliveryLocation(models.Model):
    ordering_plate = models.TextField(max_length=2000, default=None, null=True)
    phone_number = models.IntegerField()
    number_of_plate = models.IntegerField()
    delivery_location = models.TextField(max_length=2000, default=None, null=True)

# __str__ for all model (NOTICE: django 2 version)
def __str__(self):
    return f"{self.plate}, {self.recipies}, {self.dish_type}, {self.cost}, {self.added_on}, {self.number_of_plate}, {self.delivery_location}, {self.ordering_plate}, {self.phone_number}"