# Generated by Django 3.1.5 on 2021-01-16 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_navlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securitytxt', models.TextField(blank=True)),
                ('acknowledgmentstxt', models.TextField(blank=True)),
            ],
        ),
    ]
