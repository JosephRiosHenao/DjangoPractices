from django.db import models

# Create your models here.

class Themes(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
class Webs(models.Model):
    theme = models.ForeignKey(Themes,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    url = models.URLField(max_length=200,unique=True)


