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
from django.conf import settings
from schedule import views as schedule_views
from news import views as news_views
from settings.base import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # HOME
    url(r'^$', home_views.get_index, name='index'),
    url(r'^players/$', home_views.get_players, name='players'),
    url(r'^team/(?P<id>\d+)$', home_views.get_team, name='get_team'),
    url(r'^teams/$', home_views.get_teams, name='get_teams'),
    url(r'^about/', home_views.get_info, name='info'),
    url(r'^profile/', home_views.profile, name='profile'),
    url(r'^team/new/', home_views.new_team, name='newteam'),
    url(r'^players/new/', home_views.new_player, name='newplayer'),
    url(r'^team/edit/(?P<id>\d+)$', home_views.edit_team, name='edit_team'),
    url(r'^team/delete/(?P<id>\d+)$', home_views.delete_team, name='delete_team'),
    url(r'^players/edit/(?P<id>\d+)$', home_views.edit_player, name='edit-player'),
    url(r'^players/delete/(?P<id>\d+)$', home_views.delete_player, name='delete-player'),
    url(r'^newuser/$', home_views.new_user, name='new_user'),
    url(r'^edit_profile/$', home_views.edit_profile, name='edit_profile'),
    url(r'^change_your_password/$', home_views.change_your_password, name='change_your_password'),
    url(r'^login/$', home_views.login, name='login'),
    url(r'^logout/$', home_views.logout, name='logout'),
    url(r'^schedule/', schedule_views.get_schedule, name='schedule'),

    # NEWS
    url(r'^news/$', news_views.forum, name='forum'),
    url(r'^new_subject', news_views.new_subject, name='new_subject'),
    url(r'^threads/(?P<subject_id>\d+)/$', news_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', news_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', news_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', news_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', news_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', news_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', news_views.thread_vote, name='cast_vote'),

    # MEDIA
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
