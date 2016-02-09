# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0013_videoreviews_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoreviews',
            name='date_published',
            field=models.DateTimeField(null=True, verbose_name=b'Date Published', blank=True),
        ),
        migrations.AlterField(
            model_name='videoreviews',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='videoreviews',
            name='review_publisher',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
