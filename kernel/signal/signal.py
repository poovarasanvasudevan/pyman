from django.db.models.signals import pre_save
from django.dispatch import receiver

from kernel.c_models.pages import Pages
from datetime import datetime


@receiver(pre_save, sender=Pages)
def update_modified_date_for_pages(sender, instance, *args, **kwargs):
    instance.modified_on = datetime.now
