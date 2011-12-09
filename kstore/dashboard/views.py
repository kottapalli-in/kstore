from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    ctx = RequestContext(request, {})
    return render_to_response('dashboard/index.html', context_instance=ctx)
    
def addbooks(request):
    ctx = RequestContext(request, {})
    return render_to_response('dashboard/addbooks.html', context_instance=ctx)
    