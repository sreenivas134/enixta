# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoreviews', '0009_videoreviews_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='videoreviews',
            name='product_name',
            field=models.ForeignKey(to='videoreviews.Product'),
        ),
    ]
