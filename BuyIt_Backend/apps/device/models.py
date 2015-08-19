import datetime
from django.db import models

"""
Clase telefono
"""

class Device(models.Model):

    TYPE_OS = (
        ('iOS','iOS'),
        ('And','Android'),
        ('Moz','MozillaOS'),
        ('Win','Windows phone')
    )

    TYPE_DEVICE = (
        ('SP', 'Smartphone'),
        ('TB', 'Tablet')
    )

    #Intentar meter mas datos del telefono, ver si se pueden extraer.

    id_device = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=3, choices=TYPE_DEVICE, blank=True)
    os = models.CharField(max_length=3, choices=TYPE_OS, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Device, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.os + " " + self.id_device

    def users(self):
        return self.user_set.all()
    users.short_description = "User"

    def numUsers(self):
        return self.user_set.all().count()
    numUsers.short_description = "Num User"
