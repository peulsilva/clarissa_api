# Generated by Django 3.2.4 on 2021-06-03 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20210603_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 9, 47, 42, 572862)),
        ),
    ]
