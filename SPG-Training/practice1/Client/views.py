# RENDER DEFAULT
from django.shortcuts import render
# CRUD METHODS
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# DATABASE MODELS
from .models import *
# FORMS
from django import forms
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 

class ListState(ListView):
    model = State
class CreateState(SuccessMessageMixin, CreateView):
    model = State
    form = State
    fields = "__all__"
    success_message = "State created successfully"
    def get_success_url(self):        
        return reverse('State')
class ReadState(DetailView):
    model = State
class UpdateState(SuccessMessageMixin, UpdateView):
    model = State
    form = State
    fields = "__all__"
    success_message = "State updated successfully"
    def get_success_url(self):        
        return reverse('State') 
class DeleteState(SuccessMessageMixin, DeleteView):
    model = State
    form = State
    fields = "__all__"
    success_message = 'State deleted successfully' 
    def get_success_url(self):   
        return reverse('State')

class ListTypeAct(ListView):
    model = TypeAct
class CreateTypeAct(SuccessMessageMixin, CreateView):
    model = TypeAct
    form = TypeAct
    fields = "__all__"
    success_message = "TypeAct created successfully"
    def get_success_url(self):        
        return reverse('TypeAct')
class ReadTypeAct(DetailView):
    model = TypeAct
class UpdateTypeAct(SuccessMessageMixin, UpdateView):
    model = TypeAct
    form = TypeAct
    fields = "__all__"
    success_message = "TypeAct updated successfully"
    def get_success_url(self):        
        return reverse('TypeAct') 
class DeleteTypeAct(SuccessMessageMixin, DeleteView):
    model = TypeAct
    form = TypeAct
    fields = "__all__"
    success_message = 'TypeAct deleted successfully' 
    def get_success_url(self):   
        return reverse('TypeAct')

class ListTypeDoc(ListView):
    model = TypeDoc
class CreateTypeDoc(SuccessMessageMixin, CreateView):
    model = TypeDoc
    form = TypeDoc
    fields = "__all__"
    success_message = "TypeDoc created successfully"
    def get_success_url(self):        
        return reverse('TypeDoc')
class ReadTypeDoc(DetailView):
    model = TypeDoc
class UpdateTypeDoc(SuccessMessageMixin, UpdateView):
    model = TypeDoc
    form = TypeDoc
    fields = "__all__"
    success_message = "TypeDoc updated successfully"
    def get_success_url(self):        
        return reverse('TypeDoc') 
class DeleteTypeDoc(SuccessMessageMixin, DeleteView):
    model = TypeDoc
    form = TypeDoc
    fields = "__all__"
    success_message = 'TypeDoc deleted successfully' 
    def get_success_url(self):   
        return reverse('TypeDoc')


class ListClient(ListView):
    model = Client
class CreateClient(SuccessMessageMixin, CreateView):
    model = Client
    form = Client
    fields = "__all__"
    success_message = "Client created successfully"
    def get_success_url(self):        
        return reverse('Client')
class ReadClient(DetailView):
    model = Client
class UpdateClient(SuccessMessageMixin, UpdateView):
    model = Client
    form = Client
    fields = "__all__"
    success_message = "Client updated successfully"
    def get_success_url(self):        
        return reverse('Client') 
class DeleteClient(SuccessMessageMixin, DeleteView):
    model = Client
    form = Client
    fields = "__all__"
    success_message = 'Client deleted successfully' 
    def get_success_url(self):   
        return reverse('Client')