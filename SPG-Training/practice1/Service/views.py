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


class ListMovProdServ(ListView):
    model = MovProdServ
class CreateMovProdServ(SuccessMessageMixin, CreateView):
    model = MovProdServ
    form = MovProdServ
    fields = "__all__"
    success_message = "MovProdServ created successfully"
    def get_success_url(self):        
        return reverse('MovProdServ')
class ReadMovProdServ(DetailView):
    model = MovProdServ
class UpdateMovProdServ(SuccessMessageMixin, UpdateView):
    model = MovProdServ
    form = MovProdServ
    fields = "__all__"
    success_message = "MovProdServ updated successfully"
    def get_success_url(self):        
        return reverse('MovProdServ') 
class DeleteMovProdServ(SuccessMessageMixin, DeleteView):
    model = MovProdServ
    form = MovProdServ
    fields = "__all__"
    success_message = 'MovProdServ deleted successfully' 
    def get_success_url(self):   
        return reverse('MovProdServ')


class ListTypeMovement(ListView):
    model = TypeMovement
class CreateTypeMovement(SuccessMessageMixin, CreateView):
    model = TypeMovement
    form = TypeMovement
    fields = "__all__"
    success_message = "TypeMovement created successfully"
    def get_success_url(self):        
        return reverse('TypeMovement')
class ReadTypeMovement(DetailView):
    model = TypeMovement
class UpdateTypeMovement(SuccessMessageMixin, UpdateView):
    model = TypeMovement
    form = TypeMovement
    fields = "__all__"
    success_message = "TypeMovement updated successfully"
    def get_success_url(self):        
        return reverse('TypeMovement') 
class DeleteTypeMovement(SuccessMessageMixin, DeleteView):
    model = TypeMovement
    form = TypeMovement
    fields = "__all__"
    success_message = 'TypeMovement deleted successfully' 
    def get_success_url(self):   
        return reverse('TypeMovement')


class ListServicesProduct(ListView):
    model = ServicesProduct
class CreateServicesProduct(SuccessMessageMixin, CreateView):
    model = ServicesProduct
    form = ServicesProduct
    fields = "__all__"
    success_message = "ServicesProduct created successfully"
    def get_success_url(self):        
        return reverse('ServicesProduct')
class ReadServicesProduct(DetailView):
    model = ServicesProduct
class UpdateServicesProduct(SuccessMessageMixin, UpdateView):
    model = ServicesProduct
    form = ServicesProduct
    fields = "__all__"
    success_message = "ServicesProduct updated successfully"
    def get_success_url(self):        
        return reverse('ServicesProduct') 
class DeleteServicesProduct(SuccessMessageMixin, DeleteView):
    model = ServicesProduct
    form = ServicesProduct
    fields = "__all__"
    success_message = 'ServicesProduct deleted successfully' 
    def get_success_url(self):   
        return reverse('ServicesProduct')


class ListServiceProductType(ListView):
    model = ServiceProductType
class CreateServiceProductType(SuccessMessageMixin, CreateView):
    model = ServiceProductType
    form = ServiceProductType
    fields = "__all__"
    success_message = "ServiceProductType created successfully"
    def get_success_url(self):        
        return reverse('ServiceProductType')
class ReadServiceProductType(DetailView):
    model = ServiceProductType
class UpdateServiceProductType(SuccessMessageMixin, UpdateView):
    model = ServiceProductType
    form = ServiceProductType
    fields = "__all__"
    success_message = "ServiceProductType updated successfully"
    def get_success_url(self):        
        return reverse('ServiceProductType') 
class DeleteServiceProductType(SuccessMessageMixin, DeleteView):
    model = ServiceProductType
    form = ServiceProductType
    fields = "__all__"
    success_message = 'ServiceProductType deleted successfully' 
    def get_success_url(self):   
        return reverse('ServiceProductType')