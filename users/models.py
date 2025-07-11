from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return self.username
