# Generated by Django 3.1.5 on 2021-01-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210119_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='Prerequests',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]