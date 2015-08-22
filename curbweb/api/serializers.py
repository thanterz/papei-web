from django.forms import widgets
from models import purchase,shop,shop_places,product_category,product,comments,purchase_items
from rest_framework import serializers


class commentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = comments
		fields = ('id','desc','rate')

class productSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product

class productcatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product_category

class shopSerializer(serializers.HyperlinkedModelSerializer):
	products = productSerializer(many=True, read_only=True)
	class Meta:
		model=shop
		fields = ('id','name','products')