from urllib.parse import urlparse
from django.urls import URLPattern, path

from app import views

urlpatterns={
    path('createShop/',views.createShop),
    path('storeList/',views.storeList),
    path('shopdetailed/',views.shopDetailed),
    path('add_img/',views.add_img),
}
