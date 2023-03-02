from django import forms
from .models import user_signup,mynotes

class signupForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'
    

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'