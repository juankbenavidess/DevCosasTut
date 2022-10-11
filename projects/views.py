from django.shortcuts import render
# Rest Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandarduser

# Serializers
from projects.serializers import (ProjectModelSerializer, ProjectSerializer)

# Model
from projects.models import Project


# Create your views here.


class ProjectViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProjectModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandarduser]
        return (permission() for permission in permission_classes)

    def create(self, request, *args, **kwargs):
        """Create a new registry and restrict view for owner"""
        serializer = ProjectSerializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ProjectModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Project.objects.filter(user=self.request.user)
        return queryset
