# Generated by Django 2.2.12 on 2020-08-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menu_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dish_type',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]