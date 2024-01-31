from typing import Any
from django import forms
from django.core import validators

#2 other custom validator
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name Needs To start with z') # then pass the validator value to name field

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.CharField()
    verify = forms.EmailField(label='Enter again') # verifying email again
    text = forms.CharField(widget=forms.Textarea, required=False)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) # this field would not visible on the interface

# custom check
#    def clean_botcatcher(self) :
#        botcatcher = self.cleaned_data['botcatcher']
#
#        if len(botcatcher) >0:
#            raise forms.ValidationError('Error!!')
#        return botcatcher
    
    def clean(self) : # clean is used for validating data
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify']

        if email != vmail:
            raise forms.ValidationError('make sure email match')