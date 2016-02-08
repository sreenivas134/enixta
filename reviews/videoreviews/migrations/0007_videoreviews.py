# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0006_delete_videoreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoReviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_id', models.CharField(max_length=30)),
                ('review_title', models.CharField(max_length=500)),
                ('review_description', models.CharField(max_length=500)),
                ('review_publisher', models.CharField(max_length=500)),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
            ],
            options={
                'db_table': 'VideoReviews',
            },
        ),
    ]
