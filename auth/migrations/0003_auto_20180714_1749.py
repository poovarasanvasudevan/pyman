# Generated by Django 2.0.7 on 2018-07-14 12:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_component', '0002_auto_20180714_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_ref',
            field=models.TextField(default=uuid.UUID('cc7f1eea-743b-42e0-9101-52f5aa3d96e8')),
        ),
    ]