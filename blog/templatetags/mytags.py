from django import template

register = template.Library()

@register.filter
def multi(a, b):
    return a * b

@register.simple_tag
def fuckthat(a, b, c):
    return a * b * c