# Generated by Django 2.2.12 on 2020-08-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_menu_dish_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='plate',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
