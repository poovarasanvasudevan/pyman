from django.db.models.signals import pre_save
from django.dispatch import receiver

from datetime import datetime
from kernel.models import Pages


@receiver(pre_save, sender=Pages)
def update_modified_date_for_pages(sender, instance, *args, **kwargs):
    instance.modified_on = datetime.now
