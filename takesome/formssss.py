
from django import forms
from django.core import validators
#def check(value):
#    if value[0].lower() != 'a':
#        raise forms.ValidationError('Name should start with a')




class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    vmail=forms.EmailField(label="Enter email again")
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all=super().clean()
        email=all['email']
        vmail=all['vmail']
        name=all['name']

        if email != vmail:
            raise forms.ValidationError('check carefully')
