# Generated by Django 4.1.7 on 2023-03-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0017_aadharcardtable_bplstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadharcardtable',
            name='dob',
            field=models.IntegerField(),
        ),
    ]
