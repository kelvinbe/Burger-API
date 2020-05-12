from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    user = models.ForeignKey('auth.User', related_name='name', on_delete= models.CASCADE, null=True),
    ordered = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordered']

