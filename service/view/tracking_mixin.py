from service.tasks import track_task


class TrackingMixinView:
    def list(self, request, *args, **kwargs):
        track_task.delay(request)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        track_task.delay(request)
        return super().retrieve(request, *args, **kwargs)
