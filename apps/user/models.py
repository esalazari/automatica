from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    emai = models.EmailField(verbose_name="Email address", max_length=255, unique=True)


class Direction(models.Model):
    country = models.CharField(
        max_length=30, null=False, blank=False, help_text="Obligatorio"
    )
    city = models.CharField(
        max_length=30, null=False, blank=False, help_text="Obligatorio"
    )
    region = models.CharField(
        max_length=30, null=False, blank=False, help_text="Obligatorio"
    )
    postalcode = models.CharField(
        max_length=30, null=False, blank=False, help_text="Obligatorio"
    )
    commune = models.CharField(
        max_length=30, null=False, blank=False, help_text="Obligatorio"
    )
    user = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
