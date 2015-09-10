from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import commentsSerializer,productSerializer,productcatSerializer,shopSerializer,singleShopSerializer,announcementsSerializer,categoryshopSerializer,productcategoryshopSerializer
from models import comments,product,product_category,shop,announcements,shop_categories
from django.core import serializers

# Create your views here.


class commentsViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = comments.objects.all()
	serializer_class = commentsSerializer

class productViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = product.objects.all()
	serializer_class = productSerializer

class productcategoryshopViewSet(viewsets.ViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,shop_id=None,cat_id=None):
		queryset = product.objects.filter(sid_id=shop_id).filter(categ_id=cat_id)
		serializer = productcategoryshopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class productcatViewSet(viewsets.ModelViewSet):
	queryset = product_category.objects.all()
	serializer_class = productcatSerializer

class shopViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = shop.objects.all()
	serializer_class = shopSerializer

class announcementsViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = announcements.objects.all()
	serializer_class = announcementsSerializer

class singleShopViewSet(viewsets.ViewSet):
	#allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,shopid=None):
		queryset = shop.objects.filter(id=shopid)
		serializer = singleShopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class categoryshopViewSet(viewsets.ViewSet):
	def list(self,request,shop_id=None):
		queryset = product_category.objects.raw('SELECT * FROM api_product_category as apc,api_shop as ash,api_shop_categories as ascat WHERE ascat.shop_id=1 and ascat.shop_id=ash.id and apc.id=ascat.categ_id')
		serializer = categoryshopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)
	