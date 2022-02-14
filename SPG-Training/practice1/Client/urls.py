from django.urls import path
from .views import *

urlpatterns = [
    # State
    path('State/',ListState.as_view(template_name='State/data.html'),name='State'),
    path('State/create/',CreateState.as_view(template_name='State/create.html'), name="create"),
    path('State/detail/<int:pk>',ReadState.as_view(template_name='State/detail.html'),name='detail'),
    path('State/update/<int:pk>',UpdateState.as_view(template_name='State/update.html'),name='update'),
    path('State/delete/<int:pk>',DeleteState.as_view(),name='delete'),

    # TypeAct
    path('TypeAct/',ListTypeAct.as_view(template_name='TypeAct/data.html'),name='TypeAct'),
    path('TypeAct/create/',CreateTypeAct.as_view(template_name='TypeAct/create.html'), name="create"),
    path('TypeAct/detail/<int:pk>',ReadTypeAct.as_view(template_name='TypeAct/detail.html'),name='detail'),
    path('TypeAct/update/<int:pk>',UpdateTypeAct.as_view(template_name='TypeAct/update.html'),name='update'),
    path('TypeAct/delete/<int:pk>',DeleteTypeAct.as_view(),name='delete'),

    # TypeDoc
    path('TypeDoc/',ListTypeDoc.as_view(template_name='TypeDoc/data.html'),name='TypeDoc'),
    path('TypeDoc/create/',CreateTypeDoc.as_view(template_name='TypeDoc/create.html'), name="create"),
    path('TypeDoc/detail/<int:pk>',ReadTypeDoc.as_view(template_name='TypeDoc/detail.html'),name='detail'),
    path('TypeDoc/update/<int:pk>',UpdateTypeDoc.as_view(template_name='TypeDoc/update.html'),name='update'),
    path('TypeDoc/delete/<int:pk>',DeleteTypeDoc.as_view(),name='delete'),

    # Client
    path('Client/',ListClient.as_view(template_name='Client/data.html'),name='Client'),
    path('Client/create/',CreateClient.as_view(template_name='Client/create.html'), name="create"),
    path('Client/detail/<int:pk>',ReadClient.as_view(template_name='Client/detail.html'),name='detail'),
    path('Client/update/<int:pk>',UpdateClient.as_view(template_name='Client/update.html'),name='update'),
    path('Client/delete/<int:pk>',DeleteClient.as_view(),name='delete'),
]
