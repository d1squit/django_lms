from django import forms

from courses.models import Course
from students.models import Student


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'})
        }


class CreateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class UpdateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass
