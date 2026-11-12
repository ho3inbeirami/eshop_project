from django import template
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime
register = template.Library()


@register.filter(name = 'cut')
def cut(value, arg):
    return value.replace(arg,'')



@register.filter(name = 'time')
def time(value):
    return value.strftime('%H:%M:%S')



@register.filter(name = 'date')
def date(value):
    
    return datetime.datetime.date(value)#.strftime('%a, %d %b %Y')

@register.filter
def get_range(value):
    return range(value)