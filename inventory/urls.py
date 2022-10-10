from django.urls import path
from . import views

urlpatterns = [
    path('getProducts/', views.get_products),
    path('home/', views.landing_page)
]
