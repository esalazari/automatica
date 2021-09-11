from django.db import models

# Create your models here.


class machine(models.Model):
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=50)
    price = models.IntegerField(help_text="Precio del producto")
    stock = models.IntegerField(help_text="Cantidad del producto")
