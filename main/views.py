from django.shortcuts import render
from .forms import Noteform
from .models import Note

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    notes = Note.objects.all()
    return render(request, "main/home.html", {"notes": notes})

def addNote(request):
    form  = Noteform(request.POST  or None) 
    if form.is_valid():
        form.save()

    return render(request,'main/createNote.html', {"form": form} )

def details(request):
    render(request, 'main/details.html', {})