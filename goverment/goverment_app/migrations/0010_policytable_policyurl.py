# Generated by Django 4.1.6 on 2023-02-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0009_policytable_applicationtable_policyid'),
    ]

    operations = [
        migrations.AddField(
            model_name='policytable',
            name='policyurl',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
