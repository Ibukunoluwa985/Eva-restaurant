# Generated by Django 2.2.12 on 2020-08-20 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chef',
            old_name='title',
            new_name='role',
        ),
    ]
