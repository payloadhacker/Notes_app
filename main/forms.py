from django.forms import ModelForm
from .models import Note

class Noteform(ModelForm):
    class Meta: 
        model = Note
        fields = ['title', 'content', 'pinned', 'colored']
               