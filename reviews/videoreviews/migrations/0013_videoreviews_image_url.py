# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0012_product_videoreviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoreviews',
            name='image_url',
            field=models.URLField(default='None'),
            preserve_default=False,
        ),
    ]
