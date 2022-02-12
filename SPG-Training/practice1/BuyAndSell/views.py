# RENDER DEFAULT
from django.shortcuts import render
# CRUD METHODS
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# DATABASE MODELS
from .models import *
# FORmS
from django import forms
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 

class StatesList(ListView):
    model = State

class CreateState(SuccessMessageMixin, CreateView):
    model = State
    form = State
    fields = "__all__"
    success_message = "State created successfully"
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('db') # Redireccionamos a la vista principal 'leer'

class ReadState(DetailView):
    model = State

class UpdateState(SuccessMessageMixin, UpdateView):
    model = State
    form = State
    fields = "__all__"
    success_message = "State updated successfully"
    def get_success_url(self):        
        return reverse('db') 

class DeleteState(SuccessMessageMixin, DeleteView):
    model = State
    form = State
    fields = "__all__"
    success_message = 'State deleted successfully' 
    def get_success_url(self):
        # success_message = 'State deleted successfully' 
        # messages.success (self.request, (success_message))      
        return reverse('db')

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {})

