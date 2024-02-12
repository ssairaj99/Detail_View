from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView,DetailView,ListView,CreateView,UpdateView
from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
  
class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class StudentList(ListView):
    model=Student
    context_object_name='students'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
