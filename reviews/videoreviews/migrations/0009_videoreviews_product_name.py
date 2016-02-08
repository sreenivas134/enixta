# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0008_auto_20160208_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoreviews',
            name='product_name',
            field=models.CharField(default='name', max_length=1000),
            preserve_default=False,
        ),
    ]
