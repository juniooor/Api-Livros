# Generated by Django 4.2.4 on 2023-09-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Avaliacao',
        ),
        migrations.AddField(
            model_name='book',
            name='Avaliacao',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
    ]
