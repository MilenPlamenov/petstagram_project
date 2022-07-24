from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from petstagram.petstagram_auth.views import show_401

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('petstagram.main.urls')),
                  path('petstagramauth/', include('petstagram.petstagram_auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
