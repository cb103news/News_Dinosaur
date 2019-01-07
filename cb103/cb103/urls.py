"""cb103 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from myapp.views import lazybox,KeyWord2,newspaper,Newcheck
from myapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^keywordsearch/$', views.post),
    url(r'^lazybox/(\w+)/$', views.post5),
	url(r'^KeyWord2/$', views.post2),
	url(r'^newspaper/(\w+)/$', views.post3),
	url(r'^Newcheck/$', views.post8),
	url(r'^KeyWord3/(\w+)/$', views.post4),
        url(r'^vote/$', views.post6),
        url(r'^votein/(\w+)/$', views.post7),
]
