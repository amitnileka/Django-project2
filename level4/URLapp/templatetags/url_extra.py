from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#@register.filter(name="fek")
def cuta(value,arg):

    return value.replace(arg,"nilekar")


#@register.filter
@stringfilter
def lower(value):
    return value.lower()

register.filter('chota',lower)
