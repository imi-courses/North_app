# Generated by Django 5.0.2 on 2024-02-28 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('north_app', '0006_alter_grades_grade_alter_students_class_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
