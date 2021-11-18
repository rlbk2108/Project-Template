from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('photos/', include('photostock.urls')),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('account/', include('allauth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
