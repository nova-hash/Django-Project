# Generated by Django 4.1.6 on 2023-02-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goverment_app', '0012_alter_policytable_policyagency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policytable',
            name='policyTargetAudience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policytable',
            name='policytype',
            field=models.CharField(max_length=100),
        ),
    ]
