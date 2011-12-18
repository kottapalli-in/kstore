
from django.conf import settings

def theme(request):
    return {'theme': 'style3.less'}

def bank_account_details(request):
    return {'bank_account_details': getattr(settings, 'BANK_ACCOUNT_DETAILS', '')}

def search_query(request):
    return {'search_string': request.GET.get('keywords', '')}