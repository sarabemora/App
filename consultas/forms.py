from django import forms

class ConsultasForm(forms.Form):
    id = forms.CharField(label='ID', max_length=100)