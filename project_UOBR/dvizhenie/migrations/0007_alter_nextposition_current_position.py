# Generated by Django 5.0.1 on 2024-01-29 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvizhenie', '0006_alter_drillingrig_mud_alter_pad_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextposition',
            name='current_position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dvizhenie.rigposition'),
        ),
    ]
