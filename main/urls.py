from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('note/<int:pk>/', views.details, name ='details'),
    path('add/', views.addNote, name= 'create'),

]