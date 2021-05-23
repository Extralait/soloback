# Generated by Django 3.1.3 on 2021-05-23 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SOLO', '0016_auto_20210523_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocation',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='vocation',
            name='interested',
        ),
        migrations.AlterField(
            model_name='vocation',
            name='status',
            field=models.BooleanField(default=False, max_length=10, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('wait_confirm', 'Ожидание'), ('confirm', 'Подтверждено'), ('miss', 'Отклонено')], default='wait_confirm', max_length=100, verbose_name='Статус')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL, verbose_name='Работник')),
                ('vocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SOLO.vocation', verbose_name='Вокансия')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
        migrations.AddConstraint(
            model_name='interest',
            constraint=models.UniqueConstraint(fields=('owner', 'vocation'), name='unique_member_in_organization'),
        ),
    ]
