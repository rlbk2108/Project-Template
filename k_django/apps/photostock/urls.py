# app's URLs

from . import views
from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from .views import (
    password_reset_request,
    AccountPassChange,
    AccountPassChangeDone,
    AccountPassReset,
    AccountPassResetConfirm,
    AccountPassResetComplete,
    AccountPassResetDone,
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
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo-form/', PhotoCreateView.as_view(), name='photo_form'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('accounts/login/', PhotoLoginView.as_view(), name='login'),
    path('accounts/logout/', PhotoLogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('accounts/password_change/', AccountPassChange.as_view(), name='password_change'),
    path('accounts/password_change/done/', AccountPassChangeDone.as_view(), name='password_change_done'),
]