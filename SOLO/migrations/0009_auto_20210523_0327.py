# Generated by Django 3.1.3 on 2021-05-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0008_auto_20210523_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='name',
            field=models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Краткая должность'),
        ),
    ]
