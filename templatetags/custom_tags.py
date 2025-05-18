from django import template

register = template.Library()

@register.filter(name="has_permission")
def has_permission(user, permission):
  if ',' in permission:
    permission = permission.split(",")
    permission = [str(perm).strip() for perm in permission]
  return user.has_perm(permission)


@register.filter
def split(value, separator=','):
    return value.split(separator)