from django import forms
from interns.models import Intern

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = [
            'name',
            'email',
            'phone',
            'department',
            'start_date',
            'end_date'
        ]