"""StraffanAFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home import views as home_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^players/', home_views.get_players, name='players'),
    url(r'^team/', home_views.get_team_test, name='teams'),
    url(r'^about/', home_views.get_info, name='info'),
    url(r'^profile/', home_views.profile, name='profile'),
]
