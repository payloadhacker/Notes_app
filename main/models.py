from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink'),
        ('orange', 'Orange'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False)
    colored = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')

    def __str__(self):
        return self.title
