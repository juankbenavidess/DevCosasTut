from django.shortcuts import render
# Mixins ayuda con el comportamiento básico de una vista CRUD
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
# IsAuthenticated, ya que solo usuarios autenticados podrán acceder a lavista
from rest_framework.permissions import IsAuthenticated
# El usuario cumple los permisos de reclutador
from users.permissions import IsStandarduser

# Serializers
from experiences.serializers import ExperienceSerializar, ExperienceModelSerializer

# Models
from experiences.models import Experience


# Create your views here.

class ExperienceViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ExperienceModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandarduser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = ExperienceSerializar(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ExperienceModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """Restrict list to only user experience"""
        queryset = Experience.objects.filter(user=self.request.user)
        return queryset
