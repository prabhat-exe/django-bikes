from django import forms

class MyForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    course=forms.CharField()