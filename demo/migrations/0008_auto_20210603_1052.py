# Generated by Django 3.2.4 on 2021-06-03 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20210603_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('num', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('date', models.DateField(default=datetime.datetime(2021, 6, 3, 10, 52, 18, 939277))),
                ('image', models.FileField(blank=True, default=None, upload_to=None)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
