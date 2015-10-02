"""curbweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api/comments',views.commentsViewSet)
router.register(r'api/products',views.productViewSet)
router.register(r'api/categories',views.productcatViewSet)
router.register(r'api/shops',views.shopViewSet)
router.register(r'api/(?P<shopid>\d+)/shop',views.singleShopViewSet,base_name="shop")
router.register(r'api/announcements',views.announcementsViewSet)
router.register(r'api/shops/(?P<shop_id>\d+)/categories',views.categoryshopViewSet,base_name="product_category")
router.register(r'api/shops/(?P<shop_id>\d+)/categories/(?P<cat_id>\d+)',views.productcategoryshopViewSet,base_name="product")
router.register(r'api/us/(?P<uid>\d+)/pickups',views.purchaseViewSet,base_name="purchase")
router.register(r'api/menu',views.menuViewSet)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)), 
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
