# Generated by Django 2.2.3 on 2021-04-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_distanciatr'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordenadas',
            name='cor_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
