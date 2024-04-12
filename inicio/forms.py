from django import forms

class LoginForm(forms.Form):
    id = forms.CharField(label='ID', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)