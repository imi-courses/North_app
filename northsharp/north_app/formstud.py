from .models import Student
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