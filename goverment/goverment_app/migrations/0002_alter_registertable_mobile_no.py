# Generated by Django 4.1.6 on 2023-02-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertable',
            name='Mobile_no',
            field=models.BigIntegerField(max_length=13),
        ),
    ]