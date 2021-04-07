"""protwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app_two import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(app_two.urls))
    path('index',views.index,name='index'),
    path('service1',views.service1,name='service1'),
    path('service2',views.service2,name='service2'),
    path('service3',views.service3,name='service3'),
]