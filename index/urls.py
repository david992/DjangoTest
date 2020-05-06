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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, register_converter
from .views import *

register_converter(FourDigitYearConverter, 'yyyy')





urlpatterns = [
    # 参数传递
    path("<int:num1>/", index_views1),
    # re_path('(\d{2})/', music_views),
    path('<yyyy:year>/<int:month>/<int:day>', years_view),
    # 访问路径是http://localhost:8000/
    path('', index_views),
    # 访问路径是http://localhost:8000/login
    path('login/', login_views, name='login'),
    # 访问路径是http://localhost:8000/register
    path('register/', register_views, name='register'),
    path('01_temp/', temp_views),
    path('01_temp1/', temp1_views),

    path('add/',addviews,name="add"),
    path('query/',queryviews,name="add"),
    path("update/<id>", updateviews, name="update"),
    # path("update/", updateviews, name="update")
    path("delete/<id>", deleteviews, name="delete"),
    path("authors/", authorsviews, name="authors"),
    path("request/", requestviews, name="request"),
    path("form/",formviews,name="form"),
    # url(r"^form/$",formviews,name="form")
    path("test/", testviews, name="test"),
    path("session/", sessionviews),
]
