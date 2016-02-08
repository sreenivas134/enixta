# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0003_auto_20160208_1218'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoReviews',
        ),
    ]
