from django.conf.urls.defaults import *


urlpatterns = patterns('kstore.dashboard.views',
    url(r'dashboard/$', 'index', {}, name='dashboard_index'),
    url(r'dashboard/addbooks/$', 'addbooks', {}, name='dashboard_addbooks'),
)
