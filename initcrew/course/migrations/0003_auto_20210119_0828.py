# Generated by Django 3.1.5 on 2021-01-19 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210119_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='author_name',
            new_name='Author_name',
        ),
    ]