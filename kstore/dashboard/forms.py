
from django import forms
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify

from product.models import AttributeOption, Category, Price, Product, ProductAttribute, ProductImage

# any form field not in this list is considered as product attribute
NOT_PRODUCT_ATTRS = ['title', 'price', 'category', 'cover_image']

class ProductForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField(required=False)
    publisher = forms.CharField(required=False)
    published_date = forms.CharField(required=False)
    isbn = forms.CharField(required=False)
    price = forms.DecimalField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    cover_image = forms.ImageField(required=False)

    def save(self):
        data = self.cleaned_data
        site = Site.objects.get_current()

        # create product
        product = Product(name=data['title'], slug=slugify(data['title']), site=site, active=True)
        product.save()

        # create product price
        price = Price(price=data['price'], product=product)
        price.save()

        if data.get('category'):
            product.category.add(data['category'])

        if data.get('cover_image'):
            # create product image
            ProductImage.objects.create(product=product, picture=data['cover_image'])

        # check for product attributes
        for key in data:
            # if key is not product attribute or
            # value for the key is blank, goto next key
            if key in NOT_PRODUCT_ATTRS or not data[key]:
                continue

            # get the field related to the key
            field = self.fields[key]
            description = (field.label or key.replace('_', ' ')).capitalize()

            # get or create the attribute
            try:
                attribute = AttributeOption.objects.get(name=key)
            except AttributeOption.DoesNotExist:
                attribute = AttributeOption(name=key,
                                            description=description,
                                            validation='product.utils.validation_simple')
                attribute.save()

            # create product attribute
            product_attribute = ProductAttribute(product=product,
                                                 option=attribute,
                                                 value=data[key])
            product_attribute.save()
