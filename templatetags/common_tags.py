from django import template
register = template.Library()
from routine.models import routine

def get_day(value):
    return value.__dict__['day']

@register.filter(name='pick')
def pick(value):
    get_fn = routine.objects.get(pk=value)
    day = get_fn.day_set.filter(routine_id=value)
    lists = list(map(get_day, list(day)))
    print(','.join(lists))
    return ','.join(lists) 
