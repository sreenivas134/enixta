from django.db import models

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.product_name

class VideoReviews(models.Model):
	product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
	review_id = models.CharField(max_length=30)
	review_title = models.CharField(max_length=2000)
	review_description = models.TextField(help_text='Review Description')
	review_publisher = models.CharField(max_length=200,null=True,blank=True)
	image_url = models.URLField(null=True,blank=True)
	date_published = models.DateTimeField('Date Published',null=True,blank=True)

	class Meta:
		db_table = u'VideoReviews'

	def __unicode__(self):
		return self.review_id
