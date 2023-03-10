"""prueba1real URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import urls, views
from django.contrib import admin
from django.urls import path

from prueba1real.views import saludo
from prueba1real.views import despedida
from prueba1real.views import mayor
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('despedida/', despedida, name='despedida'),
    path('mayor/<int:edad>/', views.mayor, name='mayor'),
]
