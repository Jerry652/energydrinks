# Generated by Django 2.0.4 on 2018-06-17 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='Volume',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='carbonated',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='flavour',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='sparkling',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='sugar',
        ),
    ]