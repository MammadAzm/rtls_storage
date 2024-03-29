# Generated by Django 3.1.7 on 2022-03-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0028_parent_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='fromDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='tillDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationalid',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='tagposition',
            name='timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='orderDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taskresponsible',
            name='fromDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taskresponsible',
            name='tillDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='fromDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='tillDate',
            field=models.IntegerField(),
        ),
    ]
