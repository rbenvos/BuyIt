import datetime
from django.db import models
from apps.device.models import Device

"""
Clase usuario
"""


class PrivateUser(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    device = models.ManyToManyField(Device, blank=True)
    active = models.BooleanField(default=True)
    friends = models.ManyToManyField("Friend", blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(PrivateUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " - " + self.name + " " + self.last_name

    def get_all_friends(self):
        return self.friends.all()
    get_all_friends.short_description = 'Friends'

    def get_friends_activate(self):
        return self.friends.all().filter(active=True)
    get_friends_activate.short_description = 'Friends Act'

    def get_friends_desactive(self):
        return self.friends.all().filter(active=False)
    get_friends_desactive.short_description = 'Friends DesAct'

    def get_num_friends_active(self):
        return self.friends.all().filter(active=True).count()
    get_num_friends_active.short_description = 'Num Friends Act'

    def get_num_friends_desactive(self):
        return self.friends.all().filter(active=False).count()
    get_num_friends_desactive.short_description = 'Num Friends DesAct'

    def get_num_all_friends(self):
        return self.friends.all().count()
    get_num_all_friends.short_description = 'Num Friends'

    def get_devices(self):
        return self.device.all()
    get_devices.short_description = 'Devices'

    def get_num_devices(self):
        return self.device.all().count()
    get_num_devices.short_description = 'Num devices'

    def get_groups(self):
        return self.group_set.all()
    get_groups.short_description = 'Groups'

    def get_num_groups(self):
        return self.group_set.all().count()
    get_num_groups.short_description = 'Num groups'


class Friend(models.Model):
    user = models.ForeignKey("PrivateUser", default=False, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    active = models.BooleanField(default=True)