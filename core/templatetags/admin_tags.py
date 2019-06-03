from django import template
from django.conf import settings
register = template.Library()

@register.filter
def sort_apps(apps):
    count = len(apps)
    apps.sort(
        key = lambda x:
            settings.CUSTOM_PANEL_SETTINGS['app_order'].index(x['app_label'])
            if x['app_label'] in settings.CUSTOM_PANEL_SETTINGS['app_order']
            else count
    )
    return apps

@register.simple_tag
def main_color():
    return settings.CUSTOM_PANEL_SETTINGS['main_color']

@register.simple_tag
def second_color():
    return settings.CUSTOM_PANEL_SETTINGS['second_color']