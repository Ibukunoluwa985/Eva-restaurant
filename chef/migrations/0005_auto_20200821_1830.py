# Generated by Django 2.2.12 on 2020-08-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0004_chef_joined_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='facebook',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='chef',
            name='instagram',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='chef',
            name='name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chef',
            name='role',
            field=models.TextField(default=None, max_length=50, null=True),
        ),
    ]
