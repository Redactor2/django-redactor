import datetime
from django.db import models


class RedactorjsFile(models.Model):

    upload = models.FileField()
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)