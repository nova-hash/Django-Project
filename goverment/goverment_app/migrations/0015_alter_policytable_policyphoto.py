# Generated by Django 4.1.6 on 2023-02-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0014_alter_policytable_policyphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policytable',
            name='policyphoto',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
