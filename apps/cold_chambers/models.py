from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ColdChambers(models.Model):
    name = models.CharField(max_length=100)

    class CategoriesColdChambers(models.TextChoices):
        Refrigeracion = "RF", _("Refrigeración")
        Congelado = "CG", _("Congelado")

    categories = models.CharField(
        max_length=20,
        choices=CategoriesColdChambers.choices,
        help_text="Seleccione la categoria de la camara",
        verbose_name="Categoría",
    )
    dimensions = models.CharField(
        max_length=30,
        help_text="Ingrese la longitudes de la camara",
        verbose_name="Dimensiones",
    )
    camera_price = models.IntegerField(
        help_text="Precio de camara", verbose_name="Precio de camara"
    )
    installation_price = models.IntegerField(
        help_text="Precio de instalación de camara",
        verbose_name="Precio de instalación",
    )
    description = models.TextField(
        max_length=1000,
        help_text="Ingrese la descripción de la camara de frío",
        verbose_name="Descripción",
    )

    class Meta:
        verbose_name = "Camara de frío"
        verbose_name_plural = "Camaras de frío"
        ordering = ["id"]
        db_table = "cold_chamber"
