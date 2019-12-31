from django import template

register = template.Library()

@register.simple_tag
def spwm_converter(bit_resol,samples):

    from numpy import linspace
    from math import sin 

    sample_list = list(linspace(0,1,num = samples))

    table_values = list(map(lambda kT: round(sin(kT*3.14159)*(2**bit_resol)) , sample_list))

    return f'uint{bit_resol}_t lookout_sine[{samples}] = {str(table_values)}' 

    