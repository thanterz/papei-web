# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='uri',
            field=models.CharField(default='index.html', max_length=30),
            preserve_default=False,
        ),
    ]
