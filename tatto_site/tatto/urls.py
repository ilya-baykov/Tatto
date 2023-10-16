"""
URL configuration for tatto_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_us_page, name='about'),
    path('services/', views.services_page, name='services'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('sketches/', views.sketches_page, name='sketches'),
    path('reviews/', views.reviews_page, name='reviews'),
    path('prices/', views.prices_page, name='prices'),
    path('contacts/', views.contacts_page, name='contacts'),
]
