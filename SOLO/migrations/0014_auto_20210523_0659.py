# Generated by Django 3.1.3 on 2021-05-22 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0013_auto_20210523_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocation',
            name='employer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL, verbose_name='Работодатель'),
        ),
    ]