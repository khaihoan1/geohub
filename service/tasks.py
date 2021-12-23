from celery import shared_task
from revision.models import Revision


def parse_url(url):
    # todo
    ...


@shared_task
def track_task(request):

    data, action = parse_url(request)
    Revision.objects.create(action=action, data=data)
