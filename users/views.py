# https://cosasdedevs.com/posts/registro-y-autenticacion-con-django-rest-framework/
# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer, UserSignupSerializer

from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods se añade
    # el método permitido, es decir POST ó PUT ó DELETE
    # action para modificar el compo rtamiento del enrutamiento
    # detail para especificar si el detalle del modelo
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User signin"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up"""
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
