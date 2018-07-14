from django.db import models
from django.contrib.auth.models import AbstractUser
from client_module.models import Client


# Create your models here.


class CustomUser(AbstractUser):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.username
