# Generated by Django 3.1.3 on 2021-05-22 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0014_auto_20210523_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocation',
            old_name='user',
            new_name='owner',
        ),
    ]