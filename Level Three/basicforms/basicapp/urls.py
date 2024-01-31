from django.urls import path
from basicapp import views

urlpatterns = [
    path('', views.forms_name_view, name='forms'),
]
