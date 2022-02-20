from django.db import models
from authors.models import Author
# Create your models here.
class Profile(models.Model):
    alias = models.CharField(max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.alias