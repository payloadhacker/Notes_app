from django.forms import ModelForm
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Noteform(ModelForm):
    class Meta: 
        model = Note
        fields = ['title', 'content', 'pinned', 'colored']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']