from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import commentsSerializer,productSerializer,productcatSerializer,shopSerializer,singleShopSerializer,announcementsSerializer
from models import comments,product,product_category,shop,announcements
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
		queryset = shop.objects.all()
		serializer = singleShopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

