# Generated by Django 3.1.7 on 2022-02-13 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0002_asset_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='asset_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.asset'),
        ),
    ]