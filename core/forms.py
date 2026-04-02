from django import forms

class DynamicForm(forms.Form):
    name = forms.CharField(required=False)