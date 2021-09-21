from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ColdChambers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de Camara")

    class CategoriesColdChambers(models.TextChoices):
        Refrigeracion = "Refrigeración"
        Congelado = "Congelador"

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
    photo = models.ImageField(
        upload_to="camaras/",
        verbose_name="Imagen de camara de frio",
        help_text="Imagen que se mostrará en la pagina web",
    )
    camera_price = models.IntegerField(
        help_text="Precio de camara", verbose_name="Precio de camara"
    )
    installation_price = models.IntegerField(
        help_text="Precio de instalación de camara",
        verbose_name="Precio de instalación",
    )
    description = RichTextField(
        help_text="Ingrese la descripción de la camara de frío",
        verbose_name="Descripción",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Camara de frío"
        verbose_name_plural = "Camaras de frío"
        ordering = ["id"]
        db_table = "cold_chamber"
