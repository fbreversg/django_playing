from django import template
import datetime

register = template.Library()

"""
register.filter('cut', cut)
register.filter('lower', lower)
register.tag('current_time', do_current_time)
"""


# Filters
@register.filter(name='cut') # Replaces register.filter('cut', cut)
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter  # Replaces register.filter('lower', lower)
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


# Template tags
@register.tag(name="current_time") # Replaces register.tag('current_time', do_current_time)
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)
