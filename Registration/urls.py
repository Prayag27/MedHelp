from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('',views.homeHospital,name='Home'),
    path('DocReg/', views.Register_Doctor, name='ADD'),
    path('HsReg/', views.Register_Hospital, name = 'ADD'),
path('PtReg/', views.Register_patient, name = 'ADD'),
]