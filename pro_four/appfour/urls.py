from django.urls import path
from appfour import views

urlpatterns = [
    path('',views.users, name='users'),
]
