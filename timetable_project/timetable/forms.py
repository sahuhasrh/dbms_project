from django import forms
from .models import Subject, Faculty

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'is_lab', 'dept', 'hours_per_week']
        widgets = {
            'is_lab': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'hours_per_week': forms.NumberInput(attrs={'min': 1, 'max': 6}),
        }

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_name', 'dept', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }
