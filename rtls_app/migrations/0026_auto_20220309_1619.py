# Generated by Django 3.1.7 on 2022-03-09 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0025_remove_building_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='floor_id',
        ),
        migrations.AddField(
            model_name='location',
            name='zone_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.zone'),
        ),
    ]
