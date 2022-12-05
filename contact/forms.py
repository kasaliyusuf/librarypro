from django import forms
from .models import ContactTable

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = ( 
            'Name',
            'PhoneNumber',
            'Email',
            'Massege',
        
        )
