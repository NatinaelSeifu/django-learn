from django.urls import path
from basicapp import views


urlpatterns = [
    path('', views.base, name='base'),
    path('help/',views.help, name='help'),
    path('about/', views.about, name='about'),
]
