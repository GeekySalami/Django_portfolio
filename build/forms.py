from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(label="Code", widget=forms.Textarea)
