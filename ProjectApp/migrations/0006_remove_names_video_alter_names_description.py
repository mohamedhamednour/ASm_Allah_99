# Generated by Django 4.0.1 on 2022-01-16 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0005_delete_nemes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='names',
            name='Video',
        ),
        migrations.AlterField(
            model_name='names',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
