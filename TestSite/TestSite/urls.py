"""
TestSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.conf.urls import include, url
import djangoApp.views

urlpatterns = [
    path('admin/', admin.site.urls, name= 'admin'),
    path('', djangoApp.views.index, name='index'),
    path('home', djangoApp.views.index, name='home'),
    path('sith/',  djangoApp.views.sith, name='sith'),
    path('recruit/',  djangoApp.views.recruit, name='recruit'),
    path('sith/submit', djangoApp.views.submit_sith, name = 'submit_sith'),
    path('sith/<int:sith_id>', djangoApp.views.current_sith, name = 'current_sith'),
    path('recruit/save', djangoApp.views.save_recruit, name='save_recruit'),
    path('sith/<int:sith_id>/accept/<int:recruit_id>', djangoApp.views.accept_recruit, name = 'accept_recruit'),
    path('sith/info',  djangoApp.views.sith_info, name='sith_info'),
]
