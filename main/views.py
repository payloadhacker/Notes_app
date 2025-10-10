from django.shortcuts import render,redirect, get_object_or_404
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
        return redirect('home')

    return render(request,'main/createNote.html', {"form": form} )

def details(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'main/details.html', {'notes': note})


def delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'notes': note})

def edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = Noteform(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('details', pk=note.pk) 
    else:
        form = Noteform(instance=note)
    context = {
        "form": form,
        'notes': note
    }
    return render(request, 'main/edit.html', context)

