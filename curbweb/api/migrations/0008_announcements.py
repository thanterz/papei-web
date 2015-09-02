# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_shop_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(default=b'', upload_to=b'announce')),
            ],
        ),
    ]
