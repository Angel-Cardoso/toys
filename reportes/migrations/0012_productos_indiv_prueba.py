# Generated by Django 2.1 on 2018-11-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0011_auto_20181129_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_indiv',
            name='prueba',
            field=models.CharField(default='nothing', max_length=40),
        ),
    ]
