# Generated by Django 3.1.7 on 2022-03-09 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0038_auto_20220309_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zone_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.zone'),
        ),
    ]