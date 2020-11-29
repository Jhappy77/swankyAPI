# Generated by Django 3.1.3 on 2020-11-29 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ssn', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('money', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='License_Type',
            fields=[
                ('type', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('home_country', models.CharField(max_length=100)),
                ('year_founded', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.client')),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_manager', models.CharField(max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.client')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('default_img', models.URLField(blank=True, default=None, null=True)),
                ('license_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.license_type')),
                ('manufacturer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Watercraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_speed', models.IntegerField()),
                ('length', models.IntegerField()),
                ('capacity', models.CharField(max_length=100)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_type')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField()),
                ('preview_image_url', models.URLField(blank=True, default=None, max_length=120, null=True)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_type')),
            ],
            options={
                'unique_together': {('serial_no', 'type_id')},
            },
        ),
        migrations.CreateModel(
            name='Spacecraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_weight', models.IntegerField()),
                ('max_thrust', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_type')),
            ],
        ),
        migrations.CreateModel(
            name='Rents_Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rate', models.IntegerField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.partner')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_instance')),
            ],
        ),
        migrations.CreateModel(
            name='Rents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.contract')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.renter')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_instance')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.client')),
            ],
        ),
        migrations.CreateModel(
            name='Made_Spaceship_Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.manufacturer')),
                ('spacecraft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.spacecraft')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('license_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.renter')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.license_type')),
            ],
        ),
        migrations.CreateModel(
            name='Land_Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_speed', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=100)),
                ('horsepower', models.IntegerField()),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_type')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.user'),
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_count', models.IntegerField()),
                ('takeoff_speed', models.IntegerField()),
                ('seat_count', models.IntegerField()),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.vehicle_type')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_User',
            fields=[
                ('admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swankyDB.user')),
            ],
        ),
    ]