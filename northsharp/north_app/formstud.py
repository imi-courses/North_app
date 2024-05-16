from .models import Student, Subject, Grade, Employee
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput, Form


class studAdd(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "class_name","username", "password"]
        widgets = {
            "name": TextInput(attrs={
                'name': 'username',
                'class': 'forms',
                'id': 'name'
            }),
            "class_name": Select(attrs={
                'class': 'forms',
                'id': 'class'
            }),
            "username": TextInput(attrs={
                'class': 'forms',
                'id': 'log'
            }),
            "password": TextInput(attrs={
                'name': 'password',
                'class': 'forms',
                'id': 'pswd'
            }),
        }

class emplAdd(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "position", "sex", "experience", "birth_day", "Class_teacher", "subject", "role", "password"]
        widgets = {

            "name": TextInput(attrs={
                'class': 'username',
                'id': 'name'
            }),
            "position": Select(attrs={
                'class': 'password',
                'id': 'class'
            }),
            'birth_day': DateInput()
        }
class gradeAdd(ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "subject", "grade"]
        widgets = {
            "student": Select(attrs={
                'class': 'forms',
                'id': 'name'
            }),
            "subject": Select(attrs={
                'class': 'dropdown',
            }),
            "grade": Select(attrs={
                'class': 'forms',
                'id': 'class'
            }),
        }

class subjAdd(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'forms',
                'id': 'name'
            })
        }

class subjEdit(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'forms',
                'id': 'name'
            })
        }

class subjDelete(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'forms',
                'id': 'name'
            })
        }