# Generated by Django 4.0.5 on 2022-08-13 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0010_seat_user_votecast_alter_aspirant_seat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Votecast',
        ),
    ]
