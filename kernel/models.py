from django.db import models
from datetime import datetime


# Create your c_models here.
class Menu(models.Model):
    created_on: models.DateTimeField(default=datetime.now())
    module: models.IntegerField(null=True)
