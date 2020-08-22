from django.db import models

# Create your models here.

class Menu(models.Model):
    plate = models.CharField(max_length=50, default=None, null=True)
    plate_info = models.TextField(max_length=2000, default=None, null=True)
    plate_img = models.ImageField(upload_to='plate_img', default=None)
    recipies = models.CharField(max_length=50, default=None, null=True)
    dish_type = models.CharField(max_length=50, default=None, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()

class DeliveryLocation(models.Model):
    number_of_plate = models.IntegerField()
    delivery_location = models.TextField(max_length=2000, default=None, null=True)

def __str__(self):
    return f"{self.plate}, {self.recipies}, {self.dish_type}, {self.cost}, {self.added_on}, {self.number_of_plate}, {self.delivery_location}"