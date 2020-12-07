from django import template
from django.utils.safestring import mark_safe

import json
register = template.Library()

@register.filter(name='json')
def json_dumps(data, key):
    obj = ''
    try:
        obj = json.loads(data)[key]
    except BaseException:
        pass
    return obj