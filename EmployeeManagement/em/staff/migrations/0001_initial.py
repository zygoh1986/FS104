# Generated by Django 3.1.5 on 2021-01-26 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('supervisor_name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_join', models.DateField(verbose_name='Date Join')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Apprisal',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apprisal_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('overall_ratings', models.TextField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
