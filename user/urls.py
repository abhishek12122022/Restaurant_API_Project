from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('register-user', views.RegisterUser.as_view()),
    path('users/me/', views.ShowUser.as_view()),
    path('token/login/', auth_views.obtain_auth_token),
]