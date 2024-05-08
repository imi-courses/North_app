from .models import Student, Subject, Grade, Employee
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput


class studAdd(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "class_name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'forms',
                'id': 'name'
            }),
            "class_name": NumberInput(attrs={
                'class': 'forms',
                'id': 'class'
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