from django.shortcuts import render,redirect, get_object_or_404
from .forms import Noteform, MyUserCreationForm
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(author=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
        notes = Note.objects.filter(session_key=request.session.session_key, author__isnull=True)
    return render(request, 'main/home.html', {'notes': notes})

def addNote(request):
    if not request.session.session_key:
        request.session.save()

    form  = Noteform(request.POST  or None) 
    if form.is_valid():
      note= form.save(commit=False)
      if request.user.is_authenticated:
            note.author = request.user
      else:
            note.session_key = request.session.session_key
      note.save()
      messages.success(request, "Note updated successfully!")

      return redirect('home')

    return render(request,'main/createNote.html', {"form": form} )

def details(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.user.is_authenticated:
        if note.author != request.user:
            return HttpResponseForbidden("You do not have permission to view this note.")
    else:
        if note.session_key != request.session.session_key:
            return HttpResponseForbidden("You do not have permission to view this note.")
    
    return render(request, 'main/details.html', {'note': note})


def delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.user != note.author:
        return HttpResponse( "You can't delete this note.")
    else:
        if note.session_key != request.session.session_key:
            return HttpResponse( "You can't delete this note.")
    if request.method == "POST":                            
        note.delete()
        messages.success(request, "Note updated successfully!")

        return redirect('home')
    return render(request, 'main/delete.html', {'notes': note})

def edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.user != note.author:
        return HttpResponse("You can't edit this note.")
    else:
        if note.session_key != request.session.session_key:
            return HttpResponse( "You can't edit this note.")

    form = Noteform(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        messages.success(request, "Note updated successfully!")
        return redirect('details', pk=note.pk) 
    context = {
        "form": form,
        'note': note
    }
    return render(request, 'main/edit.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.Post.get('username')
        password = request.Post.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("/login/")
    return render(request, "main/login.html",{})

def signupUser(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            session_key = request.session.session_key
            if session_key:
                guest_notes = Note.objects.filter(session_key=session_key, author__isnull=True)
                for note in guest_notes:
                    note.author = user
                    note.session_key = None
                    note.save()

            messages.success(request, "Account created successfully.")
            return redirect('home')
    else:
        form = MyUserCreationForm()

    return render(request, 'main/signup.html', {'form': form})
