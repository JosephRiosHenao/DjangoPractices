from django.db import models
from Client.models import State, Client

# Create your models here.
# TipProdServ
class ServiceProductType(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)
    def __str__(self): return "[{}]-{}".format(self.ID, self.description)
# TipoMovimiento 
class TypeMovement(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)
    operator = models.CharField(max_length=1)
    def __str__(self): return "[{}]-{}-[{}]".format(self.ID, self.description, self.operator)
# ProductosServicios
class ServicesProduct(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    serviceProductTypeID = models.ForeignKey(ServiceProductType, on_delete=models.CASCADE)
    nameProdServ = models.CharField(max_length=200)
    dateIn = models.DateField()
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    observation = models.CharField(max_length=200)
    exists = models.IntegerField(max_length=12)
    def __str__(self): return "[{}]-{}".format(self.ID, self.nameProdServ)
# MovProdServ
class MovProdServ(models.Model):
    typeDocClientID = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name="typeDocClient")
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name="client")
    typeProdServID = models.ForeignKey(ServicesProduct, on_delete=models.CASCADE,  related_name="typeProdServ")
    prodServID = models.ForeignKey(ServicesProduct, on_delete=models.CASCADE, related_name="prodServ")
    dateMov = models.DateField()
    observation = models.CharField(max_length=60)
    typeMovementID = models.ForeignKey(TypeMovement, on_delete=models.CASCADE)