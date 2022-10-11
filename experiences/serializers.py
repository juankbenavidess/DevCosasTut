from rest_framework import serializers
from experiences.models import Experience


class ExperienceModelSerializer(serializers.ModelSerializer):
    """Experience model serializer"""
    """Serializer para recuperar los datos"""

    class Meta:
        model = Experience
        fields = (
            'pk',
            'date_ini',
            'date_end',
            'company',
            'description'
        )


class ExperienceSerializar(serializers.Serializer):
    """Validación de los datos y  creación de la fila en la tabla"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    company = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        exp = Experience.objects.create(**validated_data)
        return exp
