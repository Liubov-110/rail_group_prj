# Generated by Django 4.2 on 2023-04-29 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options_alter_city_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Населений пункт', 'verbose_name_plural': 'Населені пункти'},
        ),
    ]