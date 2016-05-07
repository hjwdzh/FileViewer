from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<path>[A-Za-z0-9\\\/\.\t\T\_\w\W]+)$', views.fileview, name='fileview')
]