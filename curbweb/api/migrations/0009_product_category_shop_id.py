# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_announcements'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='shop_id',
            field=models.ForeignKey(related_name='categories', default=1, to='api.shop'),
            preserve_default=False,
        ),
    ]
