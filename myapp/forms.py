from django import forms
from .models import *
  
class StudentForm(forms.ModelForm):
  
    class Meta:
        model = Student_data
        fields = ['date_of_birth', 'address', 'gender', 'mobile_no', 'blood_group', 
        'photos', 'major_cgpa', 'total_cgpa', 'linkedin', 'github']

class CGPAForm(forms.Form):
    cgpa = forms.CharField(label='Change CGPA Criteria', max_length=100)