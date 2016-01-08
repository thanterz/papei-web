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
from django.conf import settings
from rest_framework import routers
from api import views
from api.views import UserDetailsView

router = routers.DefaultRouter()
router.register(r'api/comments',views.commentsViewSet)
router.register(r'api/products',views.productViewSet)
router.register(r'api/categories',views.productcatViewSet)
router.register(r'api/shops',views.shopViewSet)
router.register(r'api/(?P<shopid>\d+)/shop',views.singleShopViewSet,base_name="shop")
router.register(r'api/announcements',views.announcementsViewSet)
router.register(r'api/shops/(?P<shop_id>\d+)/categories',views.categoryshopViewSet,base_name="product_category")
router.register(r'api/shops/(?P<shop_id>\d+)/categories/(?P<cat_id>\d+)',views.productcategoryshopViewSet,base_name="product")
router.register(r'api/pickups',views.purchasesViewSet,base_name="purchase")
router.register(r'api/pickupitems',views.purchaseItemsViewSet,base_name="purchase_items")
router.register(r'api/completed/user/(?P<uid>\d+)/pickups',views.completedPurchasesViewSet,base_name="purchase")
router.register(r'api/us/(?P<uid>\d+)/pickups',views.purchaseViewSet,base_name="purchase")
router.register(r'api/nearby',views.shopPlacesViewSet,base_name="shop_places")
router.register(r'api/nearby/lat/(?P<lat>\d+\.\d+)/lng/(?P<lng>\d+\.\d+)',views.nearbyPlacesViewSet,base_name="shop_places")
router.register(r'api/shop_categories',views.shopCategoriesViewSet,base_name='shop_categories')
#router.register(r'api/category/(?P<catid>\d+)/products',views.categoryProductsViewSet,base_name="product")
router.register(r'accounts', views.UserView, 'list')
router.register(r'api/menu',views.menuViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)), 
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^api/api/sentmail/',views.emailsent),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^password/reset/complete/$','django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),
    url(r'^password/reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
    url(r'', include('two_factor.urls', 'two_factor')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

