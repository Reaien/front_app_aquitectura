# Generated by Django 4.1.2 on 2023-12-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='nombreTitular',
            new_name='nombreContacto',
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='fonoContacto',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
