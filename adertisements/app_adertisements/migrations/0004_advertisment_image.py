# Generated by Django 4.2.4 on 2023-08-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adertisements', '0003_advertisment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]