from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('index.urls')),
    path('contact/', include ('contact.urls')),
    path('about/', include ('about.urls')),
    path('books/', include ('books.urls')),
    path('library', include ('library.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)