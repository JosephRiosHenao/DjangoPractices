from django.shortcuts import render
from DatabasePractice.models import Themes, Webs

# Create your views here.
def home(request):
    context = { "list_themes": Themes.objects.all(), "list_webs": Webs.objects.all() }
    return render(request,"pages/home.html",context)