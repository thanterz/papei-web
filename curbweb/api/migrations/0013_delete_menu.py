# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='menu',
        ),
    ]
