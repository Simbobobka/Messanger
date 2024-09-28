from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('healthcheck/', views.healthcheck),       
    path('profile/', views.profile, name='profile'),       
    path('', views.chatPage, name="home"),       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)