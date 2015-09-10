from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.

class purchase(models.Model):
	purchase_no = models.CharField(max_length=20)
	client = models.ForeignKey(User,related_name='user_id')
	pick = models.BooleanField(default=False)

class shop(models.Model):
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='slogos',default='')

class shop_places(models.Model):
	lat = models.FloatField()
	lon = models.FloatField()
	shop = models.ForeignKey(shop,related_name='shopid')

class product_category(models.Model):
	name = models.CharField(max_length=150)
	parent_cat_id = models.IntegerField()

class shop_categories(models.Model):
	shop = models.ForeignKey(shop,related_name='shops')
	categ = models.ForeignKey(product_category,related_name='categories')

class product(models.Model):
	sku = models.CharField(max_length=20)
	name = models.CharField(max_length=150)
	categ = models.ForeignKey(product_category,related_name='catid')
	price = models.FloatField()
	description = models.TextField()
	sid = models.ForeignKey(shop,related_name='products')
	photo = models.ImageField(upload_to='products',default='')

class comments(models.Model):
	desc = models.TextField()
	rate = models.IntegerField()
	client = models.ForeignKey(User,related_name='userid')
	pid = models.ForeignKey(product,related_name='productid')

class purchase_items(models.Model):
	purchase = models.ForeignKey(purchase,related_name='purchase_items')
	product = models.ForeignKey(product,related_name='products')

class announcements(models.Model):
	summary = models.TextField()
	body = models.TextField()
	image = models.ImageField(upload_to='announce',default='')


