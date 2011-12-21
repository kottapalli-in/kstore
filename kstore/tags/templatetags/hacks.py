from django import template

register = template.Library()

@register.filter
def product_attrs(product):
    attrs = product.translated_attributes('te') + product.translated_attributes()
    return dict((a.name, a.value) for a in attrs)