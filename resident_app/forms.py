from django import forms
from .models import Resident


class CreateResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date'}),
            'contract_start_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'contract_end_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'move_in_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'move_out_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }