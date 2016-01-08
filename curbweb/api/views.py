from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import commentsSerializer,productSerializer,productcatSerializer
from api.serializers import shopSerializer,singleShopSerializer,announcementsSerializer
from api.serializers import categoryshopSerializer,productcategoryshopSerializer,purchaseSerializer,menuSerializer
from api.serializers import categoryProductsSerializer,nearbyPlacesSerializer,shopCategoriesSerializer
from api.serializers import shopPlacesSerializer,purchasesSerializer,UserSerializer,UserDetailsSerializer
from api.serializers import purchaseItemsSerializer,completedPurchasesSerializer
from models import comments,product,product_category,shop,announcements,shop_categories,purchase,menu,shop_places,purchase_items
from django.core import serializers
from django.core.mail import send_mail
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_otp.decorators import otp_required
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
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,shopid=None):
		queryset = shop.objects.filter(id=shopid)
		serializer = singleShopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class categoryshopViewSet(viewsets.ViewSet):
	def list(self,request,shop_id=None):
		queryset = product_category.objects.raw('SELECT * FROM api_product_category as apc,api_shop as ash,api_shop_categories as ascat WHERE ascat.shop_id=%s and ascat.shop_id=ash.id and apc.id=ascat.categ_id',[shop_id])
		serializer = categoryshopSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class purchasesViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	#queryset = purchase.objects.all()
	serializer_class = purchasesSerializer
	authentication_classes = (TokenAuthentication,BasicAuthentication)
	def get_queryset(self):
		if(self.request.user.is_authenticated()):
			return purchase.objects.filter(client_id=self.request.user)
		else: 
			return purchase.objects.all()
        def perform_create(self, serializer):
        	serializer.save(client=self.request.user)
        def perform_update(self, serializer):
        	serializer.save(client=self.request.user)
	
class purchaseViewSet(viewsets.ViewSet):
	def list(self,request,uid=None):
		queryset = purchase.objects.filter(client_id=uid)
		serializer = purchaseSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class completedPurchasesViewSet(viewsets.ViewSet):
	def list(self,request,uid=None,pickvar=None):
                queryset = purchase.objects.filter(client=uid).filter(pick='true')
                serializer = completedPurchasesSerializer(queryset,many=True,context={'request': request})
                return Response(serializer.data)

class purchaseItemsViewSet(viewsets.ModelViewSet):
        allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
        queryset = purchase_items.objects.all()
        serializer_class = purchaseItemsSerializer

class menuViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = menu.objects.all()
	serializer_class = menuSerializer

class shopPlacesViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = shop_places.objects.all()
	serializer_class = shopPlacesSerializer

class nearbyPlacesViewSet(viewsets.ViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,lat=None,lng=None):
		queryset = shop_places.objects.raw('SELECT asp.id,lat,lon,address,geom,shop_id,ST_Distance(ST_SetSRID(ST_MakePoint(%s,%s),4326)::geography,ST_SetSRID(ST_MakePoint(lat,lon),4326)) as distance,name,logo FROM api_shop_places as asp,api_shop as ash WHERE ST_DWithin(ST_SetSRID(ST_MakePoint(%s,%s),4326)::geography,geom,200000) AND ash.id=asp.shop_id ORDER BY distance',[lat,lng,lat,lng])
		serializer = nearbyPlacesSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class shopCategoriesViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = shop_categories.objects.all()
	serializer_class = shopCategoriesSerializer
	
class categoryProductsViewSet(viewsets.ViewSet):
	def list(self,request,catid=None):
		queryset = product.objects.filter(categ=catid)
		serializer = categoryProductsSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class UserView(viewsets.ModelViewSet):
        allowed_methods = ('GET','POST', 'PUT','HEAD','OPTIONS')
	authentication_classes = (BasicAuthentication, TokenAuthentication)
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def get_permissions(self):
		# allow non-authenticated user to create via POST
		return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

@api_view(['POST'])
def emailsent(request):
	email = request.DATA.get('email',None)
	name = request.DATA.get('name')
        subject = request.DATA.get('subject')
        msg = request.DATA.get('message')	
	if email:
		send_mail(subject,msg, email,['thanterz@gmail.com'], fail_silently=False)
#		send_mail('Subject here', 'Here is the message.', 'from@example.com',['thanos@katagramma.gr'], fail_silently=False)
		return Response({"success": True})
	else:
		return Response({"success": False})


class UserDetailsView(RetrieveUpdateAPIView):

    """
    Returns User's details in JSON format.
    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    serializer_class = UserDetailsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
