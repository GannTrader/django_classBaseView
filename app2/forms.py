from django import forms

class FormBV(forms.Form):
	title = forms.CharField(max_length = 25) 
	body = forms.CharField(max_length = 255)