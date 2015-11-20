from django.conf.urls import patterns, url, include
# from django.conf.urls import patterns

# urlpatterns = patterns('Diemcaodemo.demo.views',
#                        (r'^doc/(?P<id>\w+)/', 'detail'),
#                        (r'^$', 'index'),
#                        )
from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^detail/$', views.detail, name="detail"),
]