import hashlib

from django.conf import settings
from django import template
from django.templatetags.static import StaticNode, do_static


HASH_STATIC_FILES = {}

register = template.Library()


class HashStaticNode(StaticNode):
    def url(self, context):
        path = self.path.resolve(context)
        if path not in HASH_STATIC_FILES:
            absolute_path = '{}/{}'.format(settings.STATIC_ROOT, path)
            try:
                HASH_STATIC_FILES[path] = hashlib.md5(open(absolute_path, 'rb').read()).hexdigest()
            except:
                HASH_STATIC_FILES[path] = ''

        return '{}?hash={}'.format(self.handle_simple(path), HASH_STATIC_FILES[path])


@register.tag('hash_static')
def hash_static(parser, token):
    if settings.DEBUG:
        return do_static(parser, token)
    else:
        return HashStaticNode.handle_token(parser, token)
