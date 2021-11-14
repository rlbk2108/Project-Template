from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('accounts/', include('allauth.urls')),
    path('photos/', include('photostock.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
