from django.db import models

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    role = models.CharField(max_length=50, default=None, null=True)
    chef_img = models.ImageField(upload_to='chef_img')
    instagram = models.CharField(max_length=250, default=None, null=True)
    facebook = models.CharField(max_length=250, default=None, null=True)
    joined_on = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.name}, {self.role}, {self.joined_on}"