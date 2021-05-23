# Generated by Django 3.1.3 on 2021-05-22 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0012_auto_20210523_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocation',
            name='interested',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Интересуются'),
        ),
        migrations.AlterField(
            model_name='vocation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
