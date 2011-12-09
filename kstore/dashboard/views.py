from django.contrib.sites.models import Site
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.defaultfilters import slugify

from product.models import Product, Price


def index(request):
    ctx = RequestContext(request, {})
    return render_to_response('dashboard/index.html', context_instance=ctx)


def addbooks(request):
    ctx = RequestContext(request, {})
    site = Site.objects.get_current()
    if request.method == 'POST':
        post_data = request.POST
        data = zip(post_data.getlist('title'),
                    post_data.getlist('author'),
                    post_data.getlist('publisher'),
                    post_data.getlist('published_date'),
                    post_data.getlist('isbn'),
                    post_data.getlist('price'))
        data = [item for item in data if item[0].strip()]
        import pdb;pdb.set_trace()
        for data in data:
            product = Product(name=data[0], slug=slugify(data[0]), site=site, active=True)
            product.save()
            price = Price(price=data[5], product=product)
            price.save()
        redirect('dashboard_addbooks')
    return render_to_response('dashboard/addbooks.html', context_instance=ctx)
