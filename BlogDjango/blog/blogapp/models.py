from django.db import models
from django.contrib.auth.forms import UserCreationForm

class Post(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()




