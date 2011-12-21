from django import template

register = template.Library()

@register.filter
def product_attrs(product):
    return dict((a.name, a.value) for a in product.translated_attributes())