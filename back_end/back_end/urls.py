from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

prefix_api = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{prefix_api}auth/', include('auth_custom.urls')),
    path(f'{prefix_api}', include('lessons.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
