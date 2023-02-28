from django import forms
from .models import user_signup

class signupForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'