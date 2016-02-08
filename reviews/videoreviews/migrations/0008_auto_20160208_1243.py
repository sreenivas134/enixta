# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0007_videoreviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoreviews',
            name='review_description',
            field=models.TextField(help_text=b'Review Description'),
        ),
        migrations.AlterField(
            model_name='videoreviews',
            name='review_publisher',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='videoreviews',
            name='review_title',
            field=models.CharField(max_length=2000),
        ),
    ]
