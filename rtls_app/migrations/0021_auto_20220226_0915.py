# Generated by Django 3.1.7 on 2022-02-26 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rtls_app', '0020_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='floor',
            old_name='sequence_id',
            new_name='index',
        ),
        migrations.RenameField(
            model_name='zone',
            old_name='zone_enum_id',
            new_name='type_enum_id',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='id',
        ),
        migrations.RemoveField(
            model_name='building',
            name='building_enum_id',
        ),
        migrations.RemoveField(
            model_name='building',
            name='id',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='id',
        ),
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.RemoveField(
            model_name='taskresponsible',
            name='id',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='id',
        ),
        migrations.AddField(
            model_name='building',
            name='status_enum_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='building_status_enum', to='rtls_app.enumeration'),
        ),
        migrations.AddField(
            model_name='building',
            name='type_enum_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='building_type_enum', to='rtls_app.enumeration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='floor',
            name='capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='status_enum_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_status_enum', to='rtls_app.enumeration'),
        ),
        migrations.AddField(
            model_name='person',
            name='prefix_enum_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='person_prefix_enum', to='rtls_app.enumeration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='suffix',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='floor',
            name='floor_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inventory_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='type_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_type_enum', to='rtls_app.enumeration'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_gender_enum', to='rtls_app.enumeration'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='category_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_category_enums', to='rtls_app.enumeration'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_priority_enums', to='rtls_app.enumeration'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_status_enums', to='rtls_app.enumeration'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskresponsible',
            name='task_id',
            field=models.BigAutoField(primary_key=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='zone',
            name='zone_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Machine',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='asset_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtls_app.asset', unique=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_status_enum', to='rtls_app.enumeration'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='type_enum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_type_enum', to='rtls_app.enumeration'),
        ),
    ]