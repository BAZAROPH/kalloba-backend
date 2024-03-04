"""kalloba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from website.views import (ProfilesViewSet, ProductsViewSet, CategoriesViewSet, RequestsViewSet, OrdersViewSet,
                           DiscountCodesViewSet, PaymentsViewSet, MessagesViewSet, UserViewSet, PermissionViewSet,
                           GroupViewSet, LoginView, RegisterView, UserView, BecomeSellerView, CheckObjectExistView,
                           CategoriesWithSubCatgeories)

router = routers.SimpleRouter()
router.register('profiles', ProfilesViewSet, basename='profiles')
router.register('products', ProductsViewSet, basename='products')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('requests', RequestsViewSet, basename='requests')
router.register('orders', OrdersViewSet, basename='orders')
router.register('profiles', DiscountCodesViewSet, basename='profiles')
router.register('payments', PaymentsViewSet, basename='payments')
router.register('messages', MessagesViewSet, basename='messages')
router.register('user', UserViewSet, basename='user')
router.register('permission', PermissionViewSet, basename='permission')
router.register('group', GroupViewSet, basename='group')

urlpatterns = [
    path('root/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/check-object-exist/', CheckObjectExistView.as_view(), name='check-object-exist'),

    # auth
    path('api/token/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register-client'),
    path('api/user/info/', UserView.as_view(), name='user-info'),
    path('api/user/update/', UserView.as_view(), name='user-info'),

    # Become seller
    path('api/seller/register-seller/', BecomeSellerView.as_view(), name='register-seller'),
    path('api/', include(router.urls)),

    # All categories
    path('api/categories-with-sub/', CategoriesWithSubCatgeories.as_view(), name='all-catgeories')
]
