from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'

    class Meta:
        unique_together = ['first_name', 'last_name']
