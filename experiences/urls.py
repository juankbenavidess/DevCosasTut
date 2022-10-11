"""Experience URLS"""

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from experiences import views

router = DefaultRouter()
router.register(r'experience', views.ExperienceViewSet, basename='experience')

urlpatterns = [
    path('', include(router.urls))
]
