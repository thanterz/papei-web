# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_product_category_shop_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product_category',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='shop_categories',
            name='categ',
            field=models.ForeignKey(related_name='categories', to='api.product_category'),
        ),
        migrations.AddField(
            model_name='shop_categories',
            name='shop',
            field=models.ForeignKey(related_name='shops', to='api.shop'),
        ),
    ]
