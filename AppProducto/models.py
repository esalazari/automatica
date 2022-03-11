from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    codigo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Código"
    )
    descripcion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Tipo"
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
        db_table = "tipoCamara"


class Producto(models.Model):
    codigo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Código de producto"
    )
    nombre = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Nombre de producto"
    )
    dimension = models.CharField(max_length=150, verbose_name="Dimensión del producto")
    descripcion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Descripción de producto"
    )
    peso = models.IntegerField(null=True, blank=True, verbose_name="Peso de producto")
    voltaje = models.IntegerField(
        null=True, blank=True, verbose_name="Voltaje de producto"
    )
    valorUF = models.IntegerField(
        null=True, blank=True, verbose_name="Valor uf de producto"
    )
    tipo = models.ForeignKey(
        TipoProducto,
        max_length=150,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Tipo de Camara",
    )
    # Datos de Creación
    registroActivo = models.BooleanField(default=True, verbose_name="Registro Activo")
    registroFechaCreacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"
        db_table = "producto"

    def precioAntes(self):
        _precioAnterio = self.valorUF + self.valorUF * 0.2
        return _precioAnterio

    def precioIntalacion(self):
        _precioIntalacion = self.valorUF + self.valorUF * 0.07
        return _precioIntalacion
