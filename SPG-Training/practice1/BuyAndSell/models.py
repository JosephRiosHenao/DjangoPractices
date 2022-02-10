from django.db import models

# Create your models here.

# TipoDocu
class TypeDoc(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)

# TipoActividad
class TypeAct(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)

# Estado
class State(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)

# TipProdServ
class ServiceProductType(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)

# TipoMovimiento
class TypeMovement(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    description = models.CharField(max_length=200)
    operator = models.CharField(max_length=1)

# ProductosServicios
class ServicesProduct(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    serviceProductTypeID = models.ForeignKey(ServiceProductType, on_delete=models.CASCADE)
    nameProdServ = models.CharField(max_length=200)
    dateIn = models.DateField()
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    observation = models.CharField(max_length=200)
    exists = models.IntegerField(max_length=12)

# Cliente
class Client(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    typeDocID = models.ForeignKey(TypeDoc, on_delete=models.CASCADE)
    nameRS = models.CharField(max_length=200)
    typeActID = models.ForeignKey(TypeAct, on_delete=models.CASCADE)
    dateIn = models.DateField()
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    observation = models.CharField(max_length=200)

# MovProdServ
class MovProdServ(models.Model):
    typeDocClientID = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name="typeDocClient")
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name="client")
    TypeProdServID = models.ForeignKey(ServicesProduct, on_delete=models.CASCADE,  related_name="typeProdServ")
    ProdServID = models.ForeignKey(ServicesProduct, on_delete=models.CASCADE, related_name="prodServ")
    dateMov = models.DateField()
    observation = models.CharField(max_length=60)
    typeMovementID = models.ForeignKey(TypeMovement, on_delete=models.CASCADE)