
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from dashboard.forms import ProductForm
from product.models import Product, Price


def index(request):
    ctx = RequestContext(request, {})
    return render_to_response('dashboard/index.html', context_instance=ctx)


def addbooks(request):
    ProductFormSet = formset_factory(ProductForm, extra=9)

    if request.method == 'POST':
        formset = ProductFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    form.save()
        return redirect('dashboard_addbooks')
    else:
        formset = ProductFormSet()
    ctx = RequestContext(request, {'formset': formset})
    return render_to_response('dashboard/addbooks.html', context_instance=ctx)
