from django import forms
from resumeAnalysis.models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('resume',)