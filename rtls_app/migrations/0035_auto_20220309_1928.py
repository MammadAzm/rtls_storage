# Generated by Django 3.1.7 on 2022-03-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0034_auto_20220309_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
