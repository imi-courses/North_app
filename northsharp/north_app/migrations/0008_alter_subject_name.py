from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('north_app', '0007_rename_employees_employee_rename_grades_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
