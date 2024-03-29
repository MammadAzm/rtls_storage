# Generated by Django 3.1.7 on 2022-02-13 10:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enumeration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enum_id', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EnumerationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enum_type_id', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('mac_addr', models.CharField(blank=True, max_length=23, unique=True, validators=[django.core.validators.MinLengthValidator(23)])),
                ('type_enum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtls_app.enumeration')),
            ],
        ),
        migrations.AddField(
            model_name='enumeration',
            name='enum_type_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.enumerationtype'),
        ),
        migrations.AddField(
            model_name='enumeration',
            name='parent_enum_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.enumeration'),
        ),
    ]
