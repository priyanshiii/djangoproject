

from django.db import models

import uuid


class UserModel(models.Model):
    email = models.EmailField(max_length=254, default=0)
    name =  models.CharField(max_length=120, default=0)
    username = models.CharField(max_length=120,default=0)
    password = models.CharField(max_length=40,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



class SessionToken(models.Model):
	user = models.ForeignKey(UserModel)
	session_token = models.CharField(max_length=255)
	last_request_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)
	is_valid = models.BooleanField(default=True)

	def create_token(self):
		self.session_token = uuid.uuid4()

