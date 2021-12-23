from django.db import models


class Revision(models.Model):
    ACTIONS = (
        ('S', 'Search'),
        ('F', 'Filter'),
        ('V', 'View')
    )
    action = models.CharField(choices=ACTIONS, max_length=1)
    time = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
