# Generated by Django 3.1.7 on 2022-03-10 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0047_auto_20220310_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskresponsible',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtls_app.task'),
        ),
    ]
