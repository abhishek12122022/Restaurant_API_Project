from django.urls import path
from . import views

urlpatterns = [
    path("<int:orderId>", views.OrderSpecificView.as_view()),
    path("", views.OrderView.as_view()),
]
