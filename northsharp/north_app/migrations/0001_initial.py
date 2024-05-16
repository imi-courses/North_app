# Generated by Django 5.0.2 on 2024-05-16 12:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[А-Я][а-я]* [А-Я][а-я]* [А-Я][а-я]*$')])),
                ('class_name', models.IntegerField(choices=[(1, 'Первый'), (2, 'Второй'), (3, 'Третий'), (4, 'Четвертый'), (5, 'Пятый'), (6, 'Шестой'), (7, 'Седьмой'), (8, 'Восьмой'), (9, 'Девятый'), (10, 'Десятый'), (11, 'Одиннадцатый')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('login', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('student', 'Ученик'), ('teacher', 'Учитель'), ('director', 'Директор')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Имя предмета должно начинаться с заглавной буквы', regex='^[А-Я][а-я\\s\\-]*$')])),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField(choices=[(2, 'Неудовлетворительно'), (3, 'Удовлетворительно'), (4, 'Хорошо'), (5, 'Отлично')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='north_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='north_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[А-Я][а-я]* [А-Я][а-я]* [А-Я][а-я]*$')])),
                ('position', models.IntegerField(choices=[(0, 'Учитель'), (1, 'Зам. Директор'), (2, 'Директор')], default=0)),
                ('sex', models.IntegerField(choices=[(0, 'Муж'), (1, 'Жен')], default=0)),
                ('experience', models.PositiveIntegerField()),
                ('birth_day', models.DateField()),
                ('Class_teacher', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{3}(?:[А-Я])?$', message='Только трехзначное число или трехзначное число с заглавной буквой в конце')])),
                ('role', models.CharField(choices=[('student', 'Ученик'), ('teacher', 'Учитель'), ('director', 'Директор')], default='teacher', max_length=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='north_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='north_app.grade')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='north_app.student')),
            ],
        ),
    ]
