from django import forms

from teachers.models import Teacher


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
