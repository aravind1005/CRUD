from django import forms

class MyfileForm(forms.Form):
    file_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))