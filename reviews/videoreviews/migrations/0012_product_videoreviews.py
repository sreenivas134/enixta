# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0011_auto_20160208_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VideoReviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_id', models.CharField(max_length=30)),
                ('review_title', models.CharField(max_length=2000)),
                ('review_description', models.TextField(help_text=b'Review Description')),
                ('review_publisher', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
                ('product_name', models.ForeignKey(to='videoreviews.Product')),
            ],
            options={
                'db_table': 'VideoReviews',
            },
        ),
    ]
