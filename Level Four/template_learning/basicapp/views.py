from django.shortcuts import render

# Create your views here.


def index(request):
    dict1 = {'text': "Hallo Welt", 'num':"100"}
    return render(request, 'basicapp/index.html', context=dict1)

def base(request):
    return render(request, 'basicapp/base.html')

def help(request):
    return render(request, 'basicapp/help.html')

def about(request):
    return render(request, 'basicapp/about.html')