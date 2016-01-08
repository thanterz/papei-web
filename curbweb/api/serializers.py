from django.forms import widgets
from models import shop_categories,purchase,shop,shop_places,product_category,product,comments,purchase_items,announcements,menu
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth import get_user_model, authenticate


class commentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = comments
		fields = ('id','desc','rate')

class productSerializer(serializers.HyperlinkedModelSerializer):
	#categ = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = product
		fields = ('id','sku','name','url','price','description','photo','categ','sid')

class productcategoryshopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product

class productcatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product_category

class shopPlacesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = shop_places

class nearbyPlacesSerializer(serializers.HyperlinkedModelSerializer):
	distance = serializers.FloatField()
	name = serializers.CharField()
	logo = serializers.CharField()	
	class Meta:
		model = shop_places
		fields = ('id','lat','lon','address','geom','shop','distance','name','logo')

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

class categoryshopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= product_category

class purchaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = purchase
		fields = ('purchase_no','pick','date')

class purchaseItemsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = purchase_items

class completedPurchasesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = purchase
		fields = ('id','purchase_no','pick','date')

class menuSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = menu

class shopCategoriesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = shop_categories

class categoryProductsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ( 'first_name', 'last_name', 'email','id')
		read_only_fields = ('password','is_staff', 'is_superuser', 'is_active', 'date_joined','user_permissions','groups')
	def restore_object(self, attrs, instance=None):
		# call set_password on user object. Without this
		# the password will be stored in plain text.
		user = super(UserSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','username', 'email', 'first_name', 'last_name')
        #read_only_fields = ('email', )

class purchasesSerializer(serializers.ModelSerializer):
	client = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	#store = shopPlacesSerializer(source='lat')
	lat = serializers.ReadOnlyField(source='store.lat')
	lon = serializers.ReadOnlyField(source='store.lon')
        class Meta:
                model = purchase
		fields = ('purchase_no','pick','client','date','store','lat','lon')

