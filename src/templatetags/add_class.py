from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(value, arg):
    return str(value).replace("<ul>", arg)
