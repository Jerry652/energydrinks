# Generated by Django 2.0.4 on 2018-06-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(max_length=1000)),
                ('flavour', models.CharField(max_length=250)),
                ('calories', models.CharField(max_length=100)),
                ('sparkling', models.CharField(max_length=50)),
                ('Volume', models.CharField(max_length=50)),
                ('carbonated', models.CharField(max_length=50)),
                ('sugar', models.CharField(max_length=50)),
            ],
        ),
    ]
