from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^question/([0-9]+)/$', views.test, name='test'),
    url(r'^login/|singup/|ask/|popular/|new/$', views.test),
    url(r'^$', views.test),
]
