# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_no', models.CharField(max_length=20)),
                ('pick', models.BooleanField(default=False)),
                ('client_id', models.ForeignKey(related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
