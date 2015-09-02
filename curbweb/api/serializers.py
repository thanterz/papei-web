from django.forms import widgets
from models import purchase,shop,shop_places,product_category,product,comments,purchase_items,announcements
from rest_framework import serializers


class commentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = comments
		fields = ('id','desc','rate')

class productSerializer(serializers.HyperlinkedModelSerializer):
	#categ = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = product
		fields = ('id','sku','name','url','price','description','photo','categ','sid')

class productcatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product_category

class shopSerializer(serializers.HyperlinkedModelSerializer):
	products = productSerializer(many=True, read_only=True)
	class Meta:
		model=shop
		fields = ('id','name','logo','products')

class singleShopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=shop
		#fields = ('id','name','url')

class announcementsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=announcements