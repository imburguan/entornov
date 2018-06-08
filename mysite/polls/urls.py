# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

app_name = 'polls'

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.home, name='index'),
    url(r'index2/$', views.Index2View.as_view(), name='index2'),



    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='index3'),
    #url(r'index2/$', views.Index2View.as_view(), name='index3'),

    #url(r'^vote/#(\d{})$', views.vote2, name='index3'),
    #url(r'^(?P<question_id>[0-9]+)/vote/#(\d{})$', views.vote2, name='vote'),

    #url(r'^(?P<question_id>[0-9]+)/$', views.vote, name='vote'),



    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results')

    #url('', views.IndexView.as_view(), name='index'),
    #url('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #url('<int:question_id>/vote/', views.vote, name='vote'),
    #url('<int:question_id>/vote/', views.vote, name='vote'),

    ]
# Create your tests here.
