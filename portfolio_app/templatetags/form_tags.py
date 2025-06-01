# /home/siisi/portfolio/portfolio_app/templatetags/form_tags.py

from django import template


register = template.Library()

@register.filter
def add_class(field, css):
    return field.as_widget(attrs={"class": css})
