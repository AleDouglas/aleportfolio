from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def convert_markdown(value):
    config = {
        'extra': {
        'footnotes': {
        'UNIQUE_IDS': True
        },
        'fenced_code': {
        'lang_prefix': 'lang-'
        }
        },
        'toc': {
        'permalink': False
        }
    }
    return md.markdown(value, extensions=['extra', 'toc'], extension_configs=config)
