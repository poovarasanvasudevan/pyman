from django.db import models


class Client(models.Model):
    name: models.CharField(max_length=255, null=False, blank=False, default='')
    short_name: models.CharField(max_length=20, null=False, blank=False, default='')
    description: models.TextField(null=True, default='')

    class Meta(object):
        app_label = 'client_module'
