from django.contrib import admin
from django.urls import path
from .views import home, logout_user, register_user

urlpatterns = [
    path('', home, name='home'),
    #path('login', log_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
]
