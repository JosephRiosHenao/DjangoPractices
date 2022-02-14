from django.urls import path
from .views import *

urlpatterns = [

    # TypeMovement
    path('TypeMovement/',ListTypeMovement.as_view(template_name='TypeMovement/data.html'),name='TypeMovement'),
    path('TypeMovement/create/',CreateTypeMovement.as_view(template_name='TypeMovement/create.html'), name="create"),
    path('TypeMovement/detail/<int:pk>',ReadTypeMovement.as_view(template_name='TypeMovement/detail.html'),name='detail'),
    path('TypeMovement/update/<int:pk>',UpdateTypeMovement.as_view(template_name='TypeMovement/update.html'),name='update'),
    path('TypeMovement/delete/<int:pk>',DeleteTypeMovement.as_view(),name='delete'),

    # ServiceProductType
    path('ServiceProductType/',ListServiceProductType.as_view(template_name='ServiceProductType/data.html'),name='ServiceProductType'),
    path('ServiceProductType/create/',CreateServiceProductType.as_view(template_name='ServiceProductType/create.html'), name="create"),
    path('ServiceProductType/detail/<int:pk>',ReadServiceProductType.as_view(template_name='ServiceProductType/detail.html'),name='detail'),
    path('ServiceProductType/update/<int:pk>',UpdateServiceProductType.as_view(template_name='ServiceProductType/update.html'),name='update'),
    path('ServiceProductType/delete/<int:pk>',DeleteServiceProductType.as_view(),name='delete'),

    # ServicesProduct
    path('ServicesProduct/',ListServicesProduct.as_view(template_name='ServicesProduct/data.html'),name='ServicesProduct'),
    path('ServicesProduct/create/',CreateServicesProduct.as_view(template_name='ServicesProduct/create.html'), name="create"),
    path('ServicesProduct/detail/<int:pk>',ReadServicesProduct.as_view(template_name='ServicesProduct/detail.html'),name='detail'),
    path('ServicesProduct/update/<int:pk>',UpdateServicesProduct.as_view(template_name='ServicesProduct/update.html'),name='update'),
    path('ServicesProduct/delete/<int:pk>',DeleteServicesProduct.as_view(),name='delete'),

    # MovProdServ
    path('MovProdServ/',ListMovProdServ.as_view(template_name='MovProdServ/data.html'),name='MovProdServ'),
    path('MovProdServ/create/',CreateMovProdServ.as_view(template_name='MovProdServ/create.html'), name="create"),
    path('MovProdServ/detail/<int:pk>',ReadMovProdServ.as_view(template_name='MovProdServ/detail.html'),name='detail'),
    path('MovProdServ/update/<int:pk>',UpdateMovProdServ.as_view(template_name='MovProdServ/update.html'),name='update'),
    path('MovProdServ/delete/<int:pk>',DeleteMovProdServ.as_view(),name='delete'),
]