# Generated by Django 4.2 on 2023-04-28 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('travel_time', models.IntegerField()),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='cities.city')),
            ],
        ),
    ]
