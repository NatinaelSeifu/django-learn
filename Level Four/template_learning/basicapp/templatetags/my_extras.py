from django import template

register = template.Library()

@register.filter(name='Hallo')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string

    """
    return value.replace(arg,'')

# this is one method but we can use decorator
# register.filter('cut', cut) 