# Generated by Django 2.2.12 on 2020-08-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200819_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='plate_img',
            field=models.ImageField(default=True, upload_to='plate_img'),
        ),
    ]