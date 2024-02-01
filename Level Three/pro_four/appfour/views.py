from django.shortcuts import render
from appfour.models import User
from appfour.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'appfour/index.html')

# a function displays data to use.html routed from pro_four/urls.py
def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('Error')
    return render(request, 'appfour/users.html', {'form': form})