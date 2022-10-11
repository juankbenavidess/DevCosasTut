from django.urls import include, path

from rest_framework.routers import DefaultRouter

from users import views as user_views

# Default Router recibe un viewset y genera todos los paths que se necesitan automa ticamente
#
router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
