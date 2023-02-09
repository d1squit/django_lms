from django import forms

from groups.models import Group


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
