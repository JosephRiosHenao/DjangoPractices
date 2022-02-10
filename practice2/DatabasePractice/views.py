from django.shortcuts import render
from DatabasePractice.models import Themes, Webs
from . import forms

# Create your views here.
def home(request):
    context = { "list_themes": Themes.objects.all(), "list_webs": Webs.objects.all() }
    return render(request,"pages/home.html",context)

def form(request):
    formWebs = forms.FormWebs()
    if (request.method == "POST"):
        formWeb = forms.FormWebs(request.POST)
        print(dir(formWeb))
        if (formWeb.is_valid()):
            pass
    return render(request,"pages/form.html",{"formWebs":formWebs})
