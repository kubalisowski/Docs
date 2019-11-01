from django.conf.urls import url
from basicapp import views

#TEMPLATE TAGGING -- global variable (name always the same) assigned to app name
app_name = 'basicapp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]


