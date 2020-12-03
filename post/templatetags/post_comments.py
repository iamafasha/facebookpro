from django import template

register = template.Library()


# def unapproved_comments(value, arg):
#     """Removes all values of arg from the given string"""
#     return value.replace(arg, '')

# @register.inclusion_tag
# def approved_comments(value, arg):
# """Removes all values of arg from the given string"""
# return value.replace(arg, '')

@register.filter
def in_unapproved(things):
    if things:
        return things.filter(approved=False)

@register.filter
def in_approved(things):
    if things:
        return things.filter(approved=True)