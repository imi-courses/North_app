from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.forms import DateInput


class Student(models.Model):
    Class = (
        (1, 'Первый'),
        (2, 'Второй'),
        (3, 'Третий'),
        (4, 'Четвертый'),
        (5, 'Пятый'),
        (6, 'Шестой'),
        (7, 'Седьмой'),
        (8, 'Восьмой'),
        (9, 'Девятый'),
        (10, 'Десятый'),
        (11, 'Одиннадцатый')
    )

    name = models.CharField(max_length=100, validators=[
        RegexValidator(regex='^[А-Я][а-я]* [А-Я][а-я]* [А-Я][а-я]*$')])
    class_name = models.IntegerField(choices=Class, validators=[MinValueValidator(1), MaxValueValidator(11)])


    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[
        RegexValidator(regex='^[А-Я][а-я]*$', message='Имя предмета должно начинаться с заглавной буквы')])

    def __str__(self):
        return self.name


class Employee(models.Model):
    teacher = 0
    vice_director = 1
    director = 2
    male = 0
    female = 1
    Position = (
        (teacher, 'Учитель'),
        (vice_director, 'Зам. Директор'),
        (director, 'Директор'),
    )
    Sex = (
        (male, 'Муж'),
        (female, 'Жен'),
    )
    name = models.CharField(max_length=100, validators=[
        RegexValidator(regex='^[А-Я][а-я]* [А-Я][а-я]* [А-Я][а-я]*$')])
    position = models.IntegerField(default=0, choices=Position)
    sex = models.IntegerField(default=0, choices=Sex)
    experience = models.PositiveIntegerField()
    birth_day = models.DateField()
    Class_teacher = models.CharField(max_length=100, validators=[
        RegexValidator(r'^\d{3}(?:[А-Я])?$',
                       message='Только трехзначное число или трехзначное число с заглавной буквой в конце')])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    Mark = (
        (2, 'Неудовлетворительно'),
        (3, 'Удовлетворительно'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(choices=Mark)

    def __str__(self):
        return f'{self.student.class_name} - {self.subject} - {self.grade}'

class Table(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)