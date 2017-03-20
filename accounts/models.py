from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not email:
            raise ValueError('The given username must bre set')

        email = self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractUser):


    objects = AccountUserManager()