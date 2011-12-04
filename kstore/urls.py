from django.conf.urls.defaults import *

from satchmo_store.urls import urlpatterns

urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)
