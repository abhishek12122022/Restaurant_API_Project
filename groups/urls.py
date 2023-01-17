from django.urls import path
from . import views

urlpatterns = [
    path('manager/users', views.ManagerView.as_view()),
    path('manager/users/<str:userId>', views.DeleteManagerView.as_view()),
    path('delivery-crew/users', views.DeliveryCrewView.as_view()),
    path('delivery-crew/users/<str:userId>',views.DeleteDeliveryCrewView.as_view()),
]
