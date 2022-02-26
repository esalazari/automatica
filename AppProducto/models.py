from django.db import models

# Create your models here.


class Producto(models.Model):
    codigo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Código de producto"
    )
    nombre = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Nombre de producto"
    )
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
    imagen = models.ImageField(
        upload_to="imagen/% Y/% m/% d/",
        null=True,
        blank=True,
        verbose_name="Subir Imagen",
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
