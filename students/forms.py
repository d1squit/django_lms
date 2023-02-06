from django import forms

from students.models import Student

import re


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_phone(self):
        value = re.sub('[^\d]', '', self.cleaned_data.get('phone'), flags=re.IGNORECASE)
        return f'+{value[0:2]} ({value[2:5]}) {value[5:8]}-{value[8:10]}-{value[10:12]}'


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['email']

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

