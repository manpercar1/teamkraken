# Generated by Django 3.1.3 on 2020-12-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20201217_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='representacion',
            field=models.ImageField(upload_to='media', verbose_name='Ejercicio'),
        ),
    ]
