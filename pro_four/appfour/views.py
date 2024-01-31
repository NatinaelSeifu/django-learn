from django.shortcuts import render
#from django.http import HttpResponse
from appfour.models import User
# Create your views here.

def index(request):
    return render(request, 'appfour/index.html')

# a function displays data to use.html routed from pro_four/urls.py
def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'appfour/users.html', context=user_dict)