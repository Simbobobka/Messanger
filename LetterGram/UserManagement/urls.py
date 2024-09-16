from django.urls import path
from . import views
urlpatterns = [
    path('healthcheck/', views.healthcheck),    
    path('signup/', views.SignUpView.as_view(), name='signup'),    
]
