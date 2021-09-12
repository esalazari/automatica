from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Machine(models.Model):
    class CategoriesProduct(models.TextChoices):
        Refrigeracion = "RF", _("Refrigeración")
        Gastronomia = "GT", _("Gastronomía")
        Panaderia = "PD", _("Panadería")
        Acero_Inoxidable = "AI", _("Acero Inoxidable")
        Comercio = "CM", _("Comercio")

    name = models.CharField(
        max_length=200,
        help_text="Ingrese el nombre completo del producto",
        verbose_name="Nombre",
    )
    mark = models.CharField(
        max_length=50,
        help_text="Ingrese la marca del producto",
        verbose_name="Marca del producto",
    )
    price = models.IntegerField(help_text="Precio del producto", verbose_name="Precio")
    stock = models.IntegerField(help_text="Cantidad de producto")
    description = models.TextField(
        max_length=1000,
        help_text="Ingrese la descripción completa del producto",
        verbose_name="Descripción",
    )
    categories = models.CharField(
        max_length=50,
        choices=CategoriesProduct.choices,
        help_text="Categoria de producto",
        verbose_name="Categoria",
    )
    cover_image = models.ImageField(
        upload_to="Portadas/", verbose_name="Imagen de portada"
    )

    class Meta:
        verbose_name = "Maquina"
        verbose_name_plural = "Maquinas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ImageMachine(models.Model):
    image = models.ImageField(upload_to="machines/", verbose_name="Imagen")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
