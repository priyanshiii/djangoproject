

from django.db import models


class UserModel(models.Model):
    email = models.EmailField(max_length=254, default=0)
    name =  models.CharField(max_length=120, default=0)
    username = models.CharField(max_length=120,default=0)
    password = models.CharField(max_length=40,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


