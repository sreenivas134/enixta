from django import forms
from django.forms import extras
import datetime

class QueryForm(forms.Form):
	query_in = forms.CharField(label='Product',max_length=1000,required=True)
	max_reviews = forms.IntegerField(label='Max Reviews',initial=50,required=False)

