from .models import Student, Subject, Grade, Employee
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput


class studAdd(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "class_name","login", "password"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'forms',
                'id': 'name'
            }),
            "class_name": Select(attrs={
                'class': 'forms',
                'id': 'class'
            }),
            "login": TextInput(attrs={
                'class': 'forms',
                'id': 'log'
            }),
            "password": TextInput(attrs={
                'class': 'forms',
                'id': 'pswd'
            }),
        }


class emplAdd(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "position", "sex", "experience", "birth_day", "Class_teacher", "subject"]
        widgets = {
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