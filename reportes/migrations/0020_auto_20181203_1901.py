# Generated by Django 2.1 on 2018-12-03 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0019_auto_20181203_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotes',
            name='linea',
            field=models.ForeignKey(default=1, limit_choices_to={'area': 'enlotaje'}, on_delete=django.db.models.deletion.CASCADE, to='reportes.Lineas'),
        ),
    ]
