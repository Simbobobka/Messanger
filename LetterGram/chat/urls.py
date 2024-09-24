from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck/', views.healthcheck),       
    path('chating/', views.chatPage),       
]