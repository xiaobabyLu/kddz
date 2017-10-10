from django.conf.urls import  include, url

from django.contrib import admin
import kucun.views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kucun/', include('kucun.urls')),
    url(r'^$',kucun.views.love),
]
