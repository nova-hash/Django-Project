# Generated by Django 4.1.6 on 2023-02-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0005_policytable_policycast_policytable_policygender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policytable',
            name='policytype',
            field=models.CharField(max_length=30),
        ),
    ]