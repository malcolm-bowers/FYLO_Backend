"""
Definition of urls for FYLO_Backend.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('bases/', views.BaseListView.as_view(), name='bases'),
    path('base/<int:pk>', views.BaseDetailView.as_view(), name='base-detail'),
    path('battalions/', views.BattalionListView.as_view(), name='battalions'),
    path('battalion/<int:pk>', views.BattalionDetailView.as_view(), name='battalion-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('userprofile/<int:pk>/update/', views.UserProfileUpdate.as_view(), name='userprofile-update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
