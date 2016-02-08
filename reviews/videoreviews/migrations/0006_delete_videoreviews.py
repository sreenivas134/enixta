# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0005_videoreviews'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoReviews',
        ),
    ]
