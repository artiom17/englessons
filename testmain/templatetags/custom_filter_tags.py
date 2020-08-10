from django import template

register = template.Library()


@register.filter
def change_value(value_one, value_two):
    value_one = value_one + value_two
    return value_one


@register.filter
def change_last_value(value_one, value_two):
    value_one = value_one[:-1] + value_two
    return value_one