import datetime
from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    private_user = models.ForeignKey(User, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id
