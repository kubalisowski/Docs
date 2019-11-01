from django import template

register = template.Library()

### WITH DECORATORS ###
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

##### WITHOUT DECORATORS #####
### 1st param: name of filter; 2nd param: actual function
# register.filter('cut', cut)