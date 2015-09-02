# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150819_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sid',
            field=models.ForeignKey(related_name='products', to='api.shop'),
        ),
    ]
