from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'dashboard/$', 'kstore.dashboard.views.index', {}),
    (r'dashboard/addbooks/$', 'kstore.dashboard.views.addbooks', {}),
)
