from django.shortcuts import render
from basicapp.models import School,Students
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, DetailView, 
                                                                    ListView,CreateView,UpdateView,DeleteView)
# Create your views here.

class IndexView(TemplateView):
    template_name = 'base.html'

class SchoolListV(ListView):
    model = School
    context_object_name = 'schools'

class SchoolDView(DetailView):
    model = School
    context_object_name = 'school_detail'
    template_name = 'basicapp/school_detail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')

class SchoolUpdateV(UpdateView):
    model = School
    fields = ('name', 'principal')

class SchoolDelV(DeleteView):
    model = School
    success_url = reverse_lazy('basicapp:list')