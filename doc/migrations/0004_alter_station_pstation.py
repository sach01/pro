# Generated by Django 4.0.5 on 2022-07-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_alter_station_pstation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='pstation',
            field=models.CharField(max_length=20),
        ),
    ]
