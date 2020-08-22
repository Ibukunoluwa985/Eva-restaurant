from django import template
register = template.Library()

from django.utils import timezone as tz

@register.simple_tag
def get_now(request):
    return tz.now()

@register.simple_tag
def get_today(request):
    return tz.localtime(tz.now()).date()