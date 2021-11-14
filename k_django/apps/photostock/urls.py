# app URLs

from django.urls import path
from .views import (
    PhotoCreateView, 
    PhotoDetailView, 
    PhotoListView, 
    PhotoDeleteView, 
    PhotoUpdateView,
    PhotoLoginView,
    SignUpView
)


urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo-form/', PhotoCreateView.as_view(), name='photo_form'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('accounts/login/', PhotoLoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]