from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout',views.logoutWarning,name='account_logout'), #logout page url
    path('userlogout',views.logoutUser,name="logoutuser") #logout user url
]