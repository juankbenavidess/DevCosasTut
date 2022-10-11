"""Users serializers"""

from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """ Se ocupa para recuperar los datos de un elemento dado"""

    # se define el modelo al que corresponde
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


class UserLoginSerializer(serializers.Serializer):
    # Campos que van a ser requeridos
    # Campos que vamos a querer recuperar
    email = serializers.EmailField()
    password = serializers.CharField(min_length=5, max_length=64)

    # Primero validamos los datos si las credenciales son validas, caso contrario lanzará una excepción
    def validate(self, data):
        # Authenticate recibe las credenciales, sin son validas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son validas')

        # Se guarda el usuario en el contexto para luego recuperar el token
        self.context['user'] = user
        return data

    # Si es que ha sido validado se accederá al método crear
    def create(self, validated_data):
        """Generar o recuperar token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignupSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        required=False
    )
    extract = serializers.CharField(max_length=1000, required=False)

    city = serializers.CharField(max_length=250, required=False)

    country = serializers.CharField(max_length=250, required=False)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Debe introducir un número correcto de teléfono"
    )

    phone = serializers.CharField(validators=[phone_regex, ], required=False)

    password = serializers.CharField(min_length=4, max_length=64)
    password_confirmation = serializers.CharField(min_length=4, max_length=64)
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(password)

        image = None
        if 'photo' in data:
            image = data['photo']

        if image:
            if image.size > (512 * 1024):
                raise serializers.ValidationError(f"Tamaño de imagen no soportado.")

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data)
        return user
