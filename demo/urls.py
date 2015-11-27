from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^create/$', views.CreateViewGreeting.as_view(), name="create"),
    url(r'^home/$', views.ListViewGreet.as_view(), name="home"),
]