from enum import Enum

from celery import shared_task

from service.models import Service
from revision.models import Revision


class Actions(Enum):
    SEARCH = 'S'
    VIEW = 'V'
    FILTER = 'F'


def get_action(data):
    if 'search' in data:
        return Actions.SEARCH.value
    return Actions.FILTER.value


@shared_task
def track_task(data, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk and Service.objects.filter(pk=pk).exists():
        data = {'pk': int(pk)}
        action = Actions.VIEW.value
    elif data:
        action = get_action(data)
    else:
        return
    Revision.objects.create(action=action, data=data)
