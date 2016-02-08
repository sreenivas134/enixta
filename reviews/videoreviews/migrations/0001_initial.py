# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoReviews',
            fields=[
                ('review_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
    ]
