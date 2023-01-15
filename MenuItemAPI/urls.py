from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('menu-items/', views.MenuItemList.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetail.as_view()),
]
