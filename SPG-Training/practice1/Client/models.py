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
# Cliente
class Client(models.Model):
    ID = models.AutoField(primary_key=True, max_length=16)
    typeDocID = models.ForeignKey(TypeDoc, on_delete=models.CASCADE)
    nameRS = models.CharField(max_length=200)
    typeActID = models.ForeignKey(TypeAct, on_delete=models.CASCADE)
    dateIn = models.DateField()
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    observation = models.CharField(max_length=200)
