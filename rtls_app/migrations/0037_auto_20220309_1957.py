# Generated by Django 3.1.7 on 2022-03-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0036_auto_20220309_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
