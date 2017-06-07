"""my_ez_blog URL Configuration

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
from article import views
from article.views import RSSFeed


urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.home, name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', admin.site.urls),
    url(r'^archives/$', views.archives, name = 'archives'),    
    url(r'^test/$', views.test),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^search/$', views.blog_search, name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
]

'''
url()函数有四个参数，两个是必须的：regex和view，两个可选的kwargs和name
    regex：是正则表达式，用于匹配Django请求的URL，知道匹配到一个为止
    view： 当Django匹配成功就会执行指定view中的逻辑，如archives()，search()等
    kwargs：任意关键字参数可以传一个字典到目标view
    name： 命名你的URL，是URL在Django的其他地方可以使用。

'''