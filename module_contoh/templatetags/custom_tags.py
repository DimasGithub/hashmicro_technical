from django import template

register = template.Library()

@register.filter(name="has_permission")
def has_permission(user, permission):
    if isinstance(permission, str):
        permission = [perm.strip() for perm in permission.split(',')]
    if isinstance(permission, (list, tuple)):
        return any(user.has_perm(perm) for perm in permission)
    return False

@register.filter
def split(value, separator=','):
    return value.split(separator)

