from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hallo welt')

def help(request):
    helpdic = {'help_insert': "HELP PAGE"}
    return render(request, 'appTwo/help.html', context=helpdic)