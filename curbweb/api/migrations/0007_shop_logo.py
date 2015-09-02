# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150831_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='logo',
            field=models.ImageField(default=b'', upload_to=b'slogos'),
        ),
    ]
