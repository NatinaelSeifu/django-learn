from django.urls import path
from basicapp import views


app_name = 'basicapp'

urlpatterns = [
    path('', views.SchoolListV.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name= 'create'),
    path('update/<pk>/', views.SchoolUpdateV.as_view(), name= 'update'),
    path('delete/<pk>/', views.SchoolDelV.as_view(), name='delete'),

]
