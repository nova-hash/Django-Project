# Generated by Django 4.1.6 on 2023-02-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0006_alter_policytable_policytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policytable',
            name='policyname',
            field=models.CharField(max_length=120),
        ),
    ]
