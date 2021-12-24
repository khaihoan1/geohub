from enum import Enum

from celery import shared_task

from service.models import Service
from revision.models import Revision


class Actions(Enum):
    SEARCH = 'S'
    VIEW = 'V'
    FILTER = 'F'


def get_tracking_data(request):
    data = request.query_params
    if 'search' in data:
        return data, Actions.SEARCH.value
    return data, Actions.FILTER.value


@shared_task
def track_task(request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk:
        if Service.objects.filter(pk=pk).exists():
            data, action = {'pk': int(pk)}, Actions.VIEW.value
    else:
        data, action = get_tracking_data(request)
    Revision.objects.create(action=action, data=data)
