from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def forms_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do sth
            print('Validation success')
            print('Name: '+form.cleaned_data['name'] )
        
    return render(request, 'basicapp/forms_page.html', {'form':form})