from django.contrib.auth.models import BaseUserManager, User
from django.db.models.query import QuerySet


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str):
        """
        Create and save User changing username for email
        """
        user = self.model(
            email=self.normalize_email(email), username=self.normalize_email(email)
        )

        # Set password with encrypt
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
    ) -> User:
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user
