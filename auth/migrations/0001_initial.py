# Generated by Django 2.0.7 on 2018-07-14 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_ref', models.TextField(default=uuid.UUID('eb3cd492-c3d1-4fc6-8779-9abacec4b16e'))),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
    ]
