# Generated by Django 4.2.4 on 2023-09-13 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bosssok_avalicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bosssok',
            name='avalicao',
        ),
    ]