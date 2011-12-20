"""Simple wrapper for standard checkout as implemented in payment.views"""

from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import confirm, payship
    
offline = config_get_group('PAYMENT_OFFLINE')
    
def pay_ship_info(request):
    return payship.simple_pay_ship_info(request, config_get_group('PAYMENT_OFFLINE'), 'shop/checkout/cod/pay_ship.html')
pay_ship_info = never_cache(pay_ship_info)
    
def confirm_info(request):
    return confirm.credit_confirm_info(request, offline, template='shop/checkout/cod/confirm.html')
confirm_info = never_cache(confirm_info)

