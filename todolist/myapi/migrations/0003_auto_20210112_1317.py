# Generated by Django 3.1.5 on 2021-01-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_todolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='name',
            new_name='tasks',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(),
        ),
    ]
