from email.policy import default
from django.db import models

# Create your models here.
class TipoCamara(models.Model):
    codigo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Código"
    )
    descripcion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Descripción"
    )
    # Datos de Creación
    registroActivo = models.BooleanField(default=True, verbose_name="Registro Activo")
    registroFechaCreacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        verbose_name = "Tipo de Camara"
        verbose_name_plural = "Tipo de Camara"


class ImagenCamara(models.Model):
    imagen = models.ImageField(
        default="images/default.jpg",
        upload_to="images/camaras/%Y/%m/",
        verbose_name="imagen de Camara",
    )
    # Datos de Creación
    registroActivo = models.BooleanField(default=True, verbose_name="Registro Activo")
    registroFechaCreacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Creación"
    )

    class Meta:
        verbose_name = "imagen Camara"
        verbose_name_plural = "Imagen Camara"


class Camara(models.Model):
    codigo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Código de camara"
    )
    nombre = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Nombre de camara"
    )
    dimension = models.CharField(max_length=150, verbose_name="Dimensión del camara")
    descripcion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Descripción de camara"
    )
    peso = models.IntegerField(null=True, blank=True, verbose_name="Peso de camara")
    voltaje = models.IntegerField(
        null=True, blank=True, verbose_name="Voltaje de camara"
    )
    valorUF = models.IntegerField(verbose_name="Valor uf de camara")
    tipo = models.ForeignKey(
        TipoCamara,
        max_length=150,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Tipo de Camara",
    )
    imagen = models.ManyToManyField(
        ImagenCamara, blank=True, default=None, verbose_name="Imagen de Camara"
    )
    # Datos de Creación
    registroActivo = models.BooleanField(default=True, verbose_name="Registro Activo")
    registroFechaCreacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Camara"
        verbose_name_plural = "Camara"

    def precioAntes(self):
        _precioAnterio = self.valorUF + self.valorUF * 0.2
        return _precioAnterio

    def precioIntalacion(self):
        _precioIntalacion = self.valorUF + self.valorUF * 0.07
        return _precioIntalacion
