from django.db import models
# Importing User, which is a full User model like AbstractUser we used in our News App (same thing). It allows us to authenticate users.
# https://stackoverflow.com/questions/21514354/difference-between-abstractuser-and-abstractbaseuser-in-django
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
