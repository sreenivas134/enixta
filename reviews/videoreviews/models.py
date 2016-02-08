from django.db import models

# Create your models here.

class VideoReviews(models.Model):
	product_name = models.CharField(max_length=1000)
	review_id = models.CharField(max_length=30)
	review_title = models.CharField(max_length=2000)
	review_description = models.TextField(help_text='Review Description')
	review_publisher = models.CharField(max_length=200)
	date_published = models.DateTimeField('Date Published')

	class Meta:
		db_table = u'VideoReviews'

	def __unicode__(self):
		return self.review_id
