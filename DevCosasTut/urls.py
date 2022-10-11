""" Main URL's """
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experience'), namespace='experiences')),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
    path('', include(('extras.urls', 'extras'), namespace='extras'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
