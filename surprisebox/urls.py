"""WebCourseWorkMur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from surprisebox import views

appname = 'box'
urlpatterns = [
    path('', views.index, name='index'),
    path('delivery/', views.delivery, name='delivery'),
    path('whose_gift/', views.whose_gift, name='whose_gift'),
    path('whose_gift/male/', views.male_gift, name='male_gift'),
    path('whose_gift/female/', views.female_gift, name='female_gift'),
    path('about/', views.about, name='about'),
]
