# Generated by Django 2.2.12 on 2020-08-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_plate_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='plate_info',
            field=models.CharField(default=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='plate',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='recipies',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]
