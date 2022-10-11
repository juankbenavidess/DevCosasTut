from django.shortcuts import render
# Rest Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandarduser

# Serializers
from extras.serializers import (ExtraModelSerializer, ExtraSerializer)

# Model
from extras.models import Extra


# Create your views here.
class ExtraViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ExtraModelSerializer

    def get_permissions(self):
        """Restrict list to only user Project"""
        permission_classes = [IsAuthenticated, IsStandarduser]
        return (permission() for permission in permission_classes)

    def get_queryset(self):
        """Restrict to only user project"""
        queryset = Extra.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ExtraSerializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ExtraModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
