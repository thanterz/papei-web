# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150819_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='client',
        ),
        migrations.DeleteModel(
            name='purchase',
        ),
    ]
