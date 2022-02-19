from django.shortcuts import render

def HomePage(request):
    return render(request, 'pages/home.html', {"homePageState":True})