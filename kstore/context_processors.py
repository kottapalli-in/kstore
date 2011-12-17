
from django.conf import settings

def theme(request):
    return {'theme': 'style2.less'}


def bank_account_details(request):
    return {'bank_account_details': getattr(settings, 'BANK_ACCOUNT_DETAILS', '')}
