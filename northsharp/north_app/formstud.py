from .models import Student
from .models import Student, Subject
from django.forms import ModelForm, TextInput, NumberInput


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
class gradeAdd(ModelForm):
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