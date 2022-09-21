import email
from django.db import models

class adminAccounts(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
    
