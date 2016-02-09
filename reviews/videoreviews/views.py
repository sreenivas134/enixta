from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
import json
from django.utils.safestring import mark_safe
from youtube.youtubeapi import youtube_search
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from models import VideoReviews, Product
import csv
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
				  results = youtube_search(product, max_reviews)  #get the Reviews from YouTube api
				  SaveResult(results,product)                     #sending results to save
				except HttpError, e:
				  print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
	else:
		form = forms.QueryForm
	products = Product.objects.all()
	reviews = VideoReviews.objects.all()
	return render(request,'reviews/products.html',{'products':products, 'reviews':reviews, 'form':form})

def SaveResult(values,product):
	try:
		product_id = Product.objects.only('id').get(product_name__iexact=product)  #check whether the product is
	except Product.DoesNotExist:                                                   #existing or not
		product_id = None
	if not product_id:
		product_id = Product.objects.create(product_name=product) #creating product if it is not existing

	#writing Data to CSV file
	csfile = open('reviews.csv','wb')
	review_csv = csv.DictWriter(csfile,values[0].keys())
	review_csv.writeheader()
	for review in values:
		newdict = {}
		for key, data in review.iteritems():
			newdict[key] = data.encode('utf-8')
		review_csv.writerow(newdict)
	csfile.close()

	#Start Writing csv data to database
	read = open('reviews.csv','rb+')
	headers = [x.strip() for x in read.next().split(',')]
	for line in csv.reader(read):
		line = [x.strip() for x in line]
		review = dict(zip(headers,line))
		review_id = review.get('id','')
		existing = VideoReviews.objects.filter(review_id__iexact=review_id)
		if not existing:
			data = VideoReviews(
				product_name=product_id,
				review_id=review.get('id',''),
				review_title=review.get('title',''),
				review_description=review.get('description',''),
				review_publisher=review.get('publisher',''),
				image_url=review.get('image_url',''),
				date_published=review.get('date_published',None)
				)

			data.save()

def Delete(request):    #to delete the review from the UI
	review_id = json.loads(request.POST['review_id'])
	try:
		VideoReviews.objects.filter(review_id=review_id).delete()
		return HttpResponse(json.dumps({'status':'true'}),content_type='application/json')
	except Exception as e:
		return HttpResponse(json.dumps({'status':'false'}),content_type='application/json')


