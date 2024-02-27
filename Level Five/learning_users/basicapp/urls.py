from django.urls import path
from basicapp import views

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]
