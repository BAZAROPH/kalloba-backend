from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from website.models import (Profiles, Products, Categories, Requests, Orders, DiscountCodes, Payments, Messages, User,
                            Permission, Group)


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD


class ProfilesSerializer(ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class RequestsSerializer(ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class DiscountCodesSerializer(ModelSerializer):
    class Meta:
        model = DiscountCodes
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    """Serializer who get email and password for login request"""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=None)


class RegisterClientSerializer(serializers.Serializer):
    """Serializer who get user information for registration"""
    last_name = serializers.CharField(required=True, max_length=255)
    first_name = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True, max_length=255)
    contact = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)


class BecomeSellerSerializer(serializers.Serializer):
    """Serializer who get feature seller and save in database seller ans store infos"""

    seller_last_name = serializers.CharField(required=True, max_length=255)
    seller_first_name = serializers.CharField(required=True, max_length=255)
    seller_contact = serializers.CharField(required=True, max_length=255)
    seller_email = serializers.EmailField(required=True, max_length=255)
    seller_password = serializers.CharField(required=True, max_length=255)

    store_name = serializers.CharField(required=True, max_length=255)
    store_manager_contact = serializers.CharField(required=True, max_length=255)
    store_other_contact = serializers.CharField(required=False, allow_blank=True, max_length=255)
    store_address = serializers.CharField(required=True, max_length=255)
    store_email = serializers.EmailField(required=True, max_length=255)
    store_status = serializers.CharField(required=True, max_length=255)


class CheckObjectExistSerialize(serializers.Serializer):
    """Serializer who get object attribute or return True if it exists"""
    email = serializers.EmailField(required=False, max_length=255)
    id = serializers.IntegerField(required=False)
    model = serializers.CharField(required=True, max_length=255)
