from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to="images/", null=True ,blank=True)
    bio = models.TextField(max_length=100, blank=True)