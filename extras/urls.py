"""Experience URLS"""

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from extras import views

router = DefaultRouter()
router.register(r'extra', views.ExtraViewSet, basename='extra')

urlpatterns = [
    path('', include(router.urls))
]