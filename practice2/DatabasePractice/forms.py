from django import forms

class FormWebs(forms.Form):
    name = forms.CharField()
    theme = forms.CharField()
    url = forms.URLField()