# Generated by Django 3.1.7 on 2022-03-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0031_auto_20220309_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enumeration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
