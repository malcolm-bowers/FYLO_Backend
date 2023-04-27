from django.urls import path
from . import views

urlpatterns = [
    path('file/', views.getFile),
    path('base/', views.getBase),
    path('base/add/', views.addBase),
    path('user/', views.getUser),
    path('user/add/', views.addUser.as_view()),
]