# Generated by Django 5.0.1 on 2024-02-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvizhenie', '0009_alter_rigposition_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pad',
            name='number',
            field=models.CharField(),
        ),
    ]