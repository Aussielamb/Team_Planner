# Generated by Django 5.0.4 on 2024-05-11 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('welcome', '0002_location_phone_number_location_physical_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='welcome.teamname'),
        ),
    ]
