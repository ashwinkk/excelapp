"""myproject URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
from adminacc import views as adminviews
from userapp import urls as userurls
from events import urls as eventurls
from newsfeed import urls as feedurls
from gallery import urls as galleryurls
from leaderboards import views as leaderboardviews
from adminacc import urls as adminurls
from funzone import urls as funzoneurls
from leaderboards import urls as leaderboardurls


urlpatterns = [
    url(r'^webadmin/', include(admin.site.urls)),
    url(r'^admin/',include(adminurls)),
    # url(r'^leaders/$',leaderboardviews.game_leaderboard),
    url(r'^leaderboards/',include(leaderboardurls)),
    # url(r'^competitions/$','leaderboards.views.events_list'),
    url(r'^events/',include(eventurls)),
    url(r'^funzone/',include(funzoneurls)),
    url(r'^users/',include(userurls)),
    # url(r'^chat/$',adminviews.chat),
    url(r'^feeds/',include(feedurls)),
    url(r'^gallery/',include(galleryurls)),
] + static(MEDIA_URL,document_root=MEDIA_ROOT)
