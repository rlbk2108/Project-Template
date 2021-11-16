# app URLs

from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from .views import (
    PasswordChangeView,
    PhotoCreateView, 
    PhotoDetailView, 
    PhotoListView, 
    PhotoDeleteView, 
    PhotoUpdateView,
    PhotoLoginView,
    PhotoLogoutView,
    SignUpView
)


urlpatterns = [
    path('login/', PhotoLoginView.as_view(), name='login'),
    path('accounts/logout/', PhotoLogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo-form/', PhotoCreateView.as_view(), name='photo_form'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]