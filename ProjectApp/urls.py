"""APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from typing import List, Union

from django.contrib import admin
import django.urls
from django.db import router

from ProjectApp import  views
from django.urls import path, include, URLResolver, URLPattern
from django.conf.urls.static import static
from django.conf import settings



urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('BaseSite', views.BaseSite, name='base'),
    path('nameByid/<int:Id_name>',views.NamesByid,name='nameByid'),
    path('Azkar', views.Azkar, name='Azkar'),
    # path('shoping',views.image.as_view()),

    path('signup', views.signup, name='sign'),
    path('logout', views.logOut, name='logout'),

    path('login', views.loginbase, name='login'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

