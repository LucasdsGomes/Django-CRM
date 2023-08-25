from django.contrib import admin
from django.urls import path
from .views import home, logout_user, register_user, costumer_record, delete_customer, add_record, update_record

urlpatterns = [
    path('', home, name='home'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('record/<int:pk>', costumer_record, name='record'),
    path('delete/<int:pk>', delete_customer, name='delete_record'),
    path('add_record/', add_record, name='add_record'),  
    path('update_record/<int:pk>', update_record, name='update_record'),  
]
