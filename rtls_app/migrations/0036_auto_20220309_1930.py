# Generated by Django 3.1.7 on 2022-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0035_auto_20220309_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
