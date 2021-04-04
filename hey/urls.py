"""hey URL Configuration

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
from django.urls import path
from home import views,wviews
from home import jviews,tviews,lviews
from home import inview,unview,fviews,oview,twviews,linkviews


urlpatterns = [
    path("", views.index, name='home'),
    path("add", views.add, name='home'),
    path("just", jviews.just, name='just'),
    path("justdial", jviews.justdial, name='justdial'),
    path("wordCounter", tviews.wordCounter, name='word'),
   # path("tex", tviews.tex, name='text'),
    path("seo", tviews.seo, name='seo'),
    path("seo", lviews.seo, name='seo'),
    path("link", lviews.link, name='link'),
    path("seo", wviews.seo, name='seo'),
    path("web", wviews.web, name='web'),
    path("fire", fviews.fire, name='fire'),
    path("firehome", fviews.fhome, name='firebase'),
   # path("log", fviews.logout, name='logout'),
    path('instagram', inview.indexn, name='instagram'),
    path('insta', inview.insta, name='home'),
    path('uninsta', unview.indexun, name='uninsta'),
    path('instaa', unview.instaa, name='home'),
    path('homes', twviews.homes, name='home'),
    path('twitters', twviews.twitters, name='home'),
    path('links', linkviews.links, name='home'),
    path('linkdin', linkviews.linkdin, name='home'),
    path('click', oview.click, name='home'),
   # path('twitter', tviews.indext, name='home'),

]
