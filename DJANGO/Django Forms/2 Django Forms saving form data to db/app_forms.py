from django import forms
from django.core import validators

class ModelForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Email again:')

    def clean(self):
        all_clean_data = super().clean()  ### Must be; taking data from form
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("EMAILS NOT MATCH!")
