from django.urls import path
from appthree import views

urlpatterns = [
    path('', views.help, name='index')
]
