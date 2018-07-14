from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser


# Create your c_models here.

class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True)

    user_ref = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to="profile_image", blank=True)

    class Meta(object):
        app_label = 'auth_component'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.user_ref = uuid4()
    instance.profile.save()
