# Generated by Django 3.1.3 on 2021-05-22 20:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0011_auto_20210523_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocation',
            name='interested',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Интересуются'),
        ),
    ]
