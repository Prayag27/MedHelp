from django.urls import path
from . import views
urlpatterns = [
    path('DocReg/', views.Register_Doctor, name='ADD'),
    path('HsReg/', views.Register_Hospital, name = 'ADD')
]