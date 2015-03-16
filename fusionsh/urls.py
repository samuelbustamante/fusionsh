# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin

from runs.views import RunListView, RunnerCreateView

urlpatterns = [
    url(r'^$', RunListView.as_view(), name='run_list'),
    url(r'^carrera/(?P<pk>[0-9]+)/$', RunnerCreateView.as_view(), name='runner_create'),
    url(r'^admin/', include(admin.site.urls)),
]
