# Generated by Django 3.2.4 on 2021-06-03 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_alter_data_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 10, 30, 1, 391984)),
        ),
    ]
