"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path ,re_path,include
from .views import  *

urlpatterns = [
#     主路由配置，路由分发
    path('admin/', admin.site.urls),
    # 访问路径是.../music/...时候交给music的urls
    path('music/',include('music.urls')),
    path('news/',include('news.urls')),
    path('sport/',include('sport.urls')),
#     只要路径不是以上的 则一律交给index应用
    path('',include('index.urls'))
]

