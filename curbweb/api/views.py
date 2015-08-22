from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import commentsSerializer,productSerializer,productcatSerializer,shopSerializer
from models import comments,product,product_category,shop
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
	queryset = shop.objects.all()
	serializer_class = shopSerializer