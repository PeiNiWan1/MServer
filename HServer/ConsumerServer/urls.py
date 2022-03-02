from urllib.parse import urlparse
from django.urls import URLPattern, path

from ConsumerServer import views

urlpatterns={
    
    path('login/',views.user_login),
    path("register",views.user_register),
    path('validation_session/',views.validation_session),
}