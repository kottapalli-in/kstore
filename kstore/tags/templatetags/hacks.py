from django import template
import itertools

register = template.Library()

@register.filter
def product_attrs(product):
    attrs = itertools.chain(
        product.translated_attributes('te'),
        product.translated_attributes())
    return dict((a.name, a.value) for a in attrs)