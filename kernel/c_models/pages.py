from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import HStoreField


class Pages(models.Model):
    name: models.CharField(max_length=250)
    url: models.TextField(null=True)
    modules: HStoreField(null=True)
    created_on: models.DateTimeField(default=datetime.now)
    modified_on: models.DateTimeField(default=datetime.now)

    class Meta(object):
        app_label = 'kernel'
