from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
	username = models.TextField()
	password = models.TextField()