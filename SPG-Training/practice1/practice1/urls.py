"""practice1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
# from BuyAndSell.views import *

urlpatterns = [
    path("", HomePage),
    path("", include('Client.urls')),
    path("", include('Service.urls'))
    
    
    # path('admin/',admin.site.urls),
    # # CREATE OBJECT
    # path('db/create/',CreateState.as_view(template_name='state/create.html'), name="create"),
    # # READ ALL
    # path('db/',ListState.as_view(template_name='state/data.html'),name='db'),
    # # READ OBJECT
    # path('db/detail/<int:pk>',ReadState.as_view(template_name='state/detail.html'),name='detail'),
    # # UPDATE OBJECT
    # path('db/update/<int:pk>',UpdateState.as_view(template_name='state/update.html'),name='update'),
    # # DELETE OBJECT
    # path('db/delete/<int:pk>',DeleteState.as_view(),name='delete'),
    # path('', home)
]
