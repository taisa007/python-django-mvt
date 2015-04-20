# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    url(r'^entry/$', views.entry_list, name='entry_list'), # 一覧
    url(r'^entry/add/$', views.entry_edit, name='entry_add'),  # 登録
    url(r'^entry/mod/(?P<entry_id>\d+)/$', views.entry_edit, name='entry_mod'),  # 修正
    url(r'^entry/del/(?P<entry_id>\d+)/$', views.entry_del, name='entry_del'),   # 削除
)