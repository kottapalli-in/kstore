from django.conf.urls.defaults import patterns
from satchmo_store.shop.satchmo_settings import get_satchmo_setting

ssl = get_satchmo_setting('SSL', default_value=False)

urlpatterns = patterns('',
     (r'^$', 'kstore.payment_offline.views.pay_ship_info', {'SSL':ssl}, 'OFFLINE_satchmo_checkout-step2'),
     (r'^confirm/$', 'kstore.payment_offline.views.confirm_info', {'SSL':ssl}, 'OFFLINE_satchmo_checkout-step3'),
     (r'^success/$', 'payment.views.checkout.success', {'SSL':ssl}, 'OFFLINE_satchmo_checkout-success'),
)
