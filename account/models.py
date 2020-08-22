# importing required tools
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# profile image model
class ProfileImage(models.Model):
    # the model extends the user model with one to one relation.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img', default='profile_img/avatar.png')

# __str__ for all model (NOTICE: django 2 version)
def __str__(self):
    return f"{self.profile_img}"