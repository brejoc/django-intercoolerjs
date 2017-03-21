from __future__ import unicode_literals

from django.db import models


class Counter(models.Model):
    """\
    Just a simple counter.
    """
    value = models.PositiveSmallIntegerField(default=0)
