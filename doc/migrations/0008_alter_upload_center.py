# Generated by Django 4.0.5 on 2022-08-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0007_rename_centre_upload_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='center',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
