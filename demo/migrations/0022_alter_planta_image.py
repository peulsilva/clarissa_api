# Generated by Django 3.2.4 on 2021-06-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0021_alter_planta_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='image',
            field=models.FileField(blank=True, default='planta.png', upload_to='Images'),
        ),
    ]
