from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^test/', views.test, name='test'),
    url(r'^ajax/', views.ajax, name='ajax'),
    url(r'^ajax_process/', views.ajax_process, name='ajax_process'),
)