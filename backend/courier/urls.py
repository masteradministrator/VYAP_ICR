from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework import generics, permissions, status, response, views 
from icr.views import InwardCourierRegistryViewSet, InwardCourierRegistryView
from my_auth.views import RegisterViewSet, LoginView

router = routers.DefaultRouter(trailing_slash = False)
router.register(r'/icr', InwardCourierRegistryViewSet)
router.register(r'/register', RegisterViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/vyaaptiadmin/', include(admin.site.urls)),
    url(r'^', include(router.urls), name='home'),
    #url(r'icr', InwardCourierRegistryView.as_view(), name='icr'),
    url(r'/login', LoginView.as_view(), name='login'))
