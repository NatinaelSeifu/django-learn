from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'), # 'list' is referenced in html file to create connection
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
]

