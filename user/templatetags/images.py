from django import template
from django.utils.safestring import mark_safe

import json
import os
register = template.Library()

@register.filter(name='images')
def get(user):
    path = 'media/images/' + user.nickname
    try:
        files = os.listdir(path)
    except BaseException:
        files = []
    return files