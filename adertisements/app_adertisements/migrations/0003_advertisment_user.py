# Generated by Django 4.2.4 on 2023-08-18 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_adertisements', '0002_alter_advertisment_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
