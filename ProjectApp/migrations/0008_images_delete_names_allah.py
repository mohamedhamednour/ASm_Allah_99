# Generated by Django 4.0.2 on 2022-02-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0007_names_allah_names_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Names_Allah',
        ),
    ]