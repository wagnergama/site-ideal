# Generated by Django 4.1 on 2022-09-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('at', '0002_ocorrencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencias',
            name='numero',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
