from django.contrib.auth.models import AbstractUser
from django.db import models


class Cliente(AbstractUser):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=14)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'cpf',
        'telefone',
    ]

    def __str__(self):
        return self.email
