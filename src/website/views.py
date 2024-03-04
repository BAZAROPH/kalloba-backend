from pprint import pprint

from django.contrib.auth.hashers import make_password
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.core.mail import send_mail
from datetime import date
from django.template import loader
import uuid

from kalloba.functions import get_tokens_for_user
from kalloba.serializers import (ProfilesSerializer, ProductsSerializer, CategoriesSerializer, RequestsSerializer,
                                 OrdersSerializer, DiscountCodesSerializer, PaymentsSerializer, MessagesSerializer,
                                 UserSerializer, PermissionSerializer, EmailTokenObtainPairSerializer,
                                 LoginSerializer, RegisterClientSerializer, BecomeSellerSerializer,
                                 CheckObjectExistSerialize)
from .models import (Profiles, Products, Categories, Requests, Orders, DiscountCodes, Payments, Messages, User,
                     Permission, Group, Stores, SubCategories)


# Create your views here.

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class ProfilesViewSet(ModelViewSet):
    serializer_class = ProfilesSerializer

    def get_queryset(self):
        return Profiles.objects.all()


class ProductsViewSet(ModelViewSet):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()


class CategoriesViewSet(ModelViewSet):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.all()


class RequestsViewSet(ModelViewSet):
    serializer_class = RequestsSerializer

    def get_queryset(self):
        return Requests.objects.all()


class OrdersViewSet(ModelViewSet):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.all()


class DiscountCodesViewSet(ModelViewSet):
    serializer_class = DiscountCodesSerializer

    def get_queryset(self):
        return DiscountCodes.objects.all()


class PaymentsViewSet(ModelViewSet):
    serializer_class = PaymentsSerializer

    def get_queryset(self):
        return Payments.objects.all()


class MessagesViewSet(ModelViewSet):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        return Messages.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        return Permission.objects.all()


class GroupViewSet(ModelViewSet):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        return Group.objects.all()


class LoginView(APIView):
    """ View who get user login email and password and connect user"""

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # verify if serializer is valid
        if serializer.is_valid():
            data = serializer.data
            # verify if email exist
            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])
                # check if password is correct
                if user.check_password(data['password']) is True:
                    return Response(get_tokens_for_user(user), status.HTTP_200_OK)
                else:
                    return Response({'error': 'Email ou mot de passe incorrecte'}, status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Email ou mot de passe incorrecte'}, status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CheckObjectExistView(APIView):
    def post(self, request):
        serializer = CheckObjectExistSerialize(data=request.data)
        if serializer is not None:
            if serializer.is_valid():
                data = serializer.data
                # email verification
                if data.get('email') is not None:
                    if data.get('model') == 'user':
                        exist = User.objects.filter(email=data.get('email')).exists()
                    elif data.get('model') == 'store':
                        exist = Stores.objects.filter(email=data.get('email')).exists()

                    return Response({'response': exist}, status.HTTP_200_OK)
                # id verification
                elif data.get('id') is not None:
                    return Response({'response': True}, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status.HTTP_200_OK)

    def get(self, request):
        # token verification
        if request.user.id:
            return Response({'response': True}, status.HTTP_200_OK)
        else:
            return Response({'response': False}, status.HTTP_200_OK)


class RegisterView(APIView):
    """View who save user"""

    def post(self, request):
        serializer = RegisterClientSerializer(data=request.data)
        # check if serializer is valid
        if serializer.is_valid():
            data = serializer.data
            # check if user exist
            if User.objects.filter(email=data['email']).exists():
                return Response({'error': 'Cet compte existe déjà'}, status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                last_name=data['last_name'],
                first_name=data['first_name'],
                password=data['password'],
                is_superuser=False,
                username=f"{data['last_name']}-{str(uuid.uuid4())}",
                email=data['email'],
                is_staff=False,
                is_active=True,
            )
            profile = Profiles(user=user, contact=data['contact'])
            profile.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """View who provide user authenticated info"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user_id = request.user.id
        user = User.objects.filter(id=user_id).select_related('profiles')
        user = user[0]
        user_info = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'contact': user.profiles.contact,
            'address': user.profiles.address,
            'birth_date': user.profiles.birth_date,
            'admin': user.is_staff
        }
        return Response(user_info, status.HTTP_200_OK)

    def patch(self, request):
        user_id = request.user.id
        user = User.objects.filter(id=user_id).select_related('profiles')
        user = user[0]
        data = request.data
        if data.get('first_name') is not None:
            user.first_name = data.get('first_name')
        if data.get('last_name') is not None:
            user.last_name = data.get('last_name')
        if data.get('address') is not None:
            user.profiles.address = data.get('address')
        if data.get('contact') is not None:
            user.profiles.contact = data.get('contact')
        if data.get('birth_date') is not None:
            user.profiles.birth_date = data.get('birth_date')
        if data.get('old_password') is not None and data.get('new_password') is not None:
            if user.check_password(data.get('old_password')):
                user.check_password = make_password(data.get('new_password'))
                return Response({'success': 'Mot de passe modifie avec succès'}, status.HTTP_200_OK)
            else:
                return Response({'error': 'Le mot de passe actuel est incorrecte'}, status.HTTP_400_BAD_REQUEST)

        user.save()
        user.profiles.save()

        user_updated = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'contact': user.profiles.contact,
            'address': user.profiles.address,
            'birth_date': user.profiles.birth_date
        }
        return Response(user_updated, status.HTTP_200_OK)


class BecomeSellerView(APIView):
    def post(self, request):
        serializer = BecomeSellerSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            if not User.objects.filter(email=data.get('seller_email')).exists():
                # create seller
                seller = User.objects.create_user(
                    first_name=data.get('seller_first_name'),
                    last_name=data.get('seller_last_name'),
                    email=data.get('seller_email'),
                    password=data.get('seller_password'),
                    username=f"{data.get('seller_last_name')}-{str(uuid.uuid4())}"
                )
                seller_profile = Profiles(
                    user=seller,
                    contact=data.get('seller_contact')
                )
                seller_profile.save()
            else:
                seller = User.objects.get(email=data.get('seller_email'))

            if not Stores.objects.filter(email=data.get('store_email')).exists():
                # create store
                store = Stores(
                    name=data.get('store_name'),
                    email=data.get('store_email'),
                    status=data.get('store_status'),
                    manager_contact=data.get('store_manager_contact'),
                    other_contact=data.get('store_other_contact'),
                    address=data.get('store_address'),
                    seller=seller,
                )
                store.save()
                # send email to seller
                html_message = loader.render_to_string('newSellerEmail.html', {
                    'last_name': data.get('seller_last_name'),
                    'first_name': data.get('seller_first_name'),
                    'current_data': date.today(),
                    'email': data.get('seller_email'),

                })
                send_mail(
                    'Ouverture de compte',
                    'Ce message est automatique, veuillez ne pas répondre',
                    from_email='Kalloba <noreply@kalloba.com>',
                    recipient_list=[data.get('seller_email')],
                    fail_silently=False,
                    html_message=html_message
                )
                return Response('Boutique enregistrée avec succès', status.HTTP_200_OK)
            else:
                return Response('Cette boutique existe déjà', status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CategoriesWithSubCatgeories(APIView):
    def get(self, request):
        parent = Categories.objects.all()
        subcategories = SubCategories.objects.filter().select_related('parent')

        categories = []
        for elt in parent:
            # filtering categories, find and save subcategorie
            middle = {
                'id': elt.id,
                'name': elt.name,
                'subcategories': [],
            }
            for sub in subcategories:
                print(sub)
                if middle['name'] == sub.parent.name:
                    middle['subcategories'].append({
                        'id': sub.id,
                        'name': sub.name
                    })

            categories.append(middle)

        return Response(categories, status.HTTP_200_OK)
