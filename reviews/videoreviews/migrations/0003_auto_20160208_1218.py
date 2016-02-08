# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0002_auto_20160208_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoreviews',
            name='review_id',
        ),
        migrations.AddField(
            model_name='videoreviews',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
