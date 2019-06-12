from django import forms

class UserLoginForm(forms.Form):
    """Form to allow users to login."""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)