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
