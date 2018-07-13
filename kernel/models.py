from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import HStoreField


# Create your c_models here.
class Menu(models.Model):
    created_on: models.DateTimeField(default=datetime.now())
    module: models.IntegerField(null=True)


class Pages(models.Model):
    name: models.CharField(max_length=250, blank=True)
    url: models.TextField(null=True, blank=True)
    modules: HStoreField(null=True, blank=True)
    created_on: models.DateTimeField(default=datetime.now)
    modified_on: models.DateTimeField(default=datetime.now)

    class Meta(object):
        app_label = 'kernel'
