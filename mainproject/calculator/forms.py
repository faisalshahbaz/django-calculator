from django import forms



class HomeForm(forms.Form):
    num1 = forms.IntegerField(required=False)
    num2 = forms.IntegerField(required=False)