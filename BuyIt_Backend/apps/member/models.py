import datetime
from django.db import models
from apps.private_user.models import PrivateUser


class Member(models.Model):
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    private_user = models.ForeignKey(PrivateUser, blank=True, null=True)
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
        return str(self.id) + ' ' + self.private_user.name + ' ' + self.private_user.last_name
