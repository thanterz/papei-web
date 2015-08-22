# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.TextField()),
                ('rate', models.IntegerField()),
                ('client', models.ForeignKey(related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('parent_cat_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='purchase_items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(related_name='products', to='api.product')),
                ('purchase', models.ForeignKey(related_name='purchase_items', to='api.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='shop_places',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('shop', models.ForeignKey(related_name='shopid', to='api.shop')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categ',
            field=models.ForeignKey(related_name='catid', to='api.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sid',
            field=models.ForeignKey(related_name='shop_id', to='api.shop'),
        ),
        migrations.AddField(
            model_name='comments',
            name='pid',
            field=models.ForeignKey(related_name='productid', to='api.product'),
        ),
    ]
