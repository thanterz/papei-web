from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import User
import uuid
# Create your models here.


class shop(models.Model):
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='slogos',default='')

class shop_places(models.Model):
	lat = models.FloatField()
	lon = models.FloatField()
	address = models.CharField(max_length=80, null=True, blank=True)
	geom = models.PointField(srid=4326, null=True, blank=True)
	objects = models.GeoManager()
	shop = models.ForeignKey(shop,related_name='shopid')

class purchase(models.Model):
	purchase_no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	client = models.ForeignKey(User,related_name='user_id')
	pick = models.BooleanField(default=False)
	date = models.DateTimeField()
	store = models.ForeignKey(shop_places,related_name='store')

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
        #cdate = models.DateTimeField(default=datetime.now(), blank=True)
	created = models.DateTimeField(auto_now_add=True)	

class menu(models.Model):
	title = models.TextField()
	content = models.TextField()
	order = models.IntegerField()
	uri = models.CharField(max_length=30)
