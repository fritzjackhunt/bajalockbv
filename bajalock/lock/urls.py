from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('company', views.company, name='company'),
    path('operations', views.operations, name='operations'),
    path('sustainability', views.sustainability, name='sustainability'),
    path('products', views.products, name='products'),

    path('contact', views.contact, name='contact'),
]