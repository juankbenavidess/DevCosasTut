from django.shortcuts import render
# Rest Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandarduser

# Serializers
from education.serializers import (EducationModelSerializer, EducationSerializer)

# Model
from education.models import Education


# Create your views here.
class EducationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EducationModelSerializer

    def get_permissions(self):
        """Restrict list to only user Education"""
        permission_classes = [IsAuthenticated, IsStandarduser]
        return (permission() for permission in permission_classes)

    def get_queryset(self):
        """Restrict to only user education"""
        queryset = Education.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = EducationSerializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = EducationModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
