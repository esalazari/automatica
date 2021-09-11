from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.managers import UserManager

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="Email address", max_length=255, unique=True)
    is_active = models.BooleanField(default=False, verbose_name="Activo")

    # Establecer el correo electrónico como inicio se sesión, remplazando username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"
        ordering = ["email"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
