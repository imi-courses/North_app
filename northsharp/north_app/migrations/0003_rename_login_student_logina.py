# Generated by Django 5.0.2 on 2024-05-16 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('north_app', '0002_employee_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='login',
            new_name='logina',
        ),
    ]
