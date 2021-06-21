from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.CharField(null=True, blank=True, default=None, max_length=55)
    first_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    last_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    email = models.CharField(null=True, blank=True, default=None, max_length=55)
    password = models.CharField(null=True, blank=True, default=None, max_length=55)
    password1 = models.CharField(null=True, blank=True, default=None, max_length=55)

    # def __str__(self):
    #   return self.email