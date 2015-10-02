# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150909_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 9, 42, 15, 390261, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
