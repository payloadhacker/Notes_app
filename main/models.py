from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content= models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    pinned = models.BooleanField(default=False)
    colored = models.CharField(max_length=20, default="white")

    def __str__(self):
        return self.title


