from django import forms
from django.forms import extras
import datetime

class QueryForm(forms.Form):
	query_in = forms.CharField(label='Enter Product Names (separated by Comma)',widget=forms.Textarea,max_length=1000,required=True)
	max_reviews = forms.IntegerField(label='Max Reviews',initial=50,required=False)

