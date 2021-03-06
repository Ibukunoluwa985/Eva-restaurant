# Generated by Django 2.2.12 on 2020-08-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, null=True)),
                ('title', models.TextField(default=True, max_length=50, null=True)),
                ('chef_img', models.ImageField(default=True, upload_to='chef_img')),
                ('instagram', models.CharField(default=True, max_length=250, null=True)),
                ('facebook', models.CharField(default=True, max_length=250, null=True)),
            ],
        ),
    ]
