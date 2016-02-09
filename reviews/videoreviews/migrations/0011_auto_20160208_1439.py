# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0010_auto_20160208_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoreviews',
            name='product_name',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='VideoReviews',
        ),
    ]
