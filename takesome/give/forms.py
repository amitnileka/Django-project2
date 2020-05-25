from django import forms

from give.models import jacob

class Newuser(forms.ModelForm):
    class Meta():
        model=jacob
        fields=['first_name','last_name']
