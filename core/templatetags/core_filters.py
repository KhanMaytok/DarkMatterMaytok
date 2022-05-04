import math
from typing import List

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=False)
@stringfilter
def make_list_from_dots(value: str) -> List[str]:
    """
    return the dot value as a list
    """
    return value.split(".")


@register.filter(is_safe=True)
@stringfilter
def format_maytok_currency(currency: str) -> str:
    """
    return the currency formatted in base 1024
    """
    currency = 0 if currency == "" or currency is None else int(currency)
    units = ['S', 'KS', 'MS', 'GS', 'TS', 'PS', 'ES', 'ZS', 'YS']
    currency = max([currency, 0])
    _pow = math.floor((math.log(currency) if currency else 0) / math.log(1024))
    _pow = min([_pow, len(units) - 1])
    currency = currency / pow(1024, _pow)

    return f"{round(currency * 100) / 100}{units[_pow]}"
