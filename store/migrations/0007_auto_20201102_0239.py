# Generated by Django 3.1.1 on 2020-11-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201101_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
