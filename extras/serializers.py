from rest_framework import serializers
from extras.models import Extra


class ExtraModelSerializer(serializers.ModelSerializer):
    """Extra Model Serializer"""

    class Meta:
        """Meta class"""
        model = Extra
        fields = (
            'pk',
            'expedition',
            'title',
            'url',
            'description',
        )


class ExtraSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    expedition = serializers.DateTimeField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=500)

    def create(self, validated_data):
        extra = Extra.objects.create(**validated_data)
        return extra
