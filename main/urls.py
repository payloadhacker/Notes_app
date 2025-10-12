from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('note/<int:pk>/', views.details, name ='details'),
    path('add/', views.addNote, name= 'create'),
    path('note/<int:pk>/delete/', views.delete, name ='delete'),
    path('note/<int:pk>/edit/', views.edit, name='edit'),
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signupUser, name='signup'),]