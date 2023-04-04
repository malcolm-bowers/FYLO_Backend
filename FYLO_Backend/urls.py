"""
Definition of urls for FYLO_Backend.
"""

from django.urls import path
from django.contrib import admin
from app import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('bases/', views.BaseListView.as_view(), name='bases'),
    path('base/<int:pk>', views.BaseDetailView.as_view(), name='base-detail'),
    path('battalions/', views.BattalionListView.as_view(), name='battalions'),
    path('battalion/<int:pk>', views.BattalionDetailView.as_view(), name='battalion-detail'),
    path('brigade/<int:pk>', views.BrigadeDetailView.as_view(), name='brigade-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('pdf/upload/', views.upload_pdf, name='upload_pdf'),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)