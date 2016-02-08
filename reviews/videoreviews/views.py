from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from . import forms
import json
from django.utils.safestring import mark_safe
from youtube.youtubeapi import youtube_search
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from models import VideoReviews


from django.utils.encoding import smart_unicode

# Create your views here.

def index(request):
	
	if request.method == 'POST':
		form = forms.QueryForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			query = data['query_in']
			max_reviews = data['max_reviews']

			products = query.split(',')

			for product in products:
				try:
				  results = youtube_search(product, max_reviews)
				  SaveResult(results,product)
				except HttpError, e:
				  print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
	else:
		form = forms.QueryForm
	return render(request,'reviews/index.html',{'reviews':'Working fine','form':form})

def SaveResult(values,product):
	for review in values:
		print review,'\n\n'
		data = VideoReviews(
			product_name=product,
			review_id=review.get('id',''),
			review_title=review.get('title',''),
			review_description=review.get('description','').encode('utf-8'),
			review_publisher=review.get('publisher',''),
			date_published=review.get('date_published','')
			)

		data.save()




