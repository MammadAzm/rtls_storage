# Generated by Django 3.1.7 on 2022-02-13 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0012_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='post_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rtls_app.post'),
            preserve_default=False,
        ),
    ]
