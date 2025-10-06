from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('notes/', NotesListView.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),



]