from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def bye(request):
    return HttpResponse("Goodbye, world. You're at the polls index.")
def time(request):
    return HttpResponse("It is now " + str(datetime.datetime.now()))
def yearsOld(request, year):
    return HttpResponse("You are " + str(datetime.datetime.now().year - int(year)) + " years old.")
def homePage(request):
    return render(request,"homePage.html",{ "name": "Django"})
def img(request):
    return render(request,"imgPage.html",{})
def forPage(request):
    # ctx = {"themes":["Django", "Python", "Java", "C++"]}
    ctx = {"themes":[]}
    return render(request,"forPage.html",ctx)