from django.db import models

# Create your models here.


class UserModel(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, default='F')
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    has_verified_mobile = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


