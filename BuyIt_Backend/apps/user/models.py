import datetime
from django.db import models
from apps.device.models import Device

"""
Clase usuario
"""
class User(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    device = models.ManyToManyField(Device, blank=True)
    active = models.BooleanField(default=True)
    #avatar = models.ImageField(blank=True)
    friends = models.ManyToManyField('User',blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " - " + self.name + " " + self.last_name

    def getAllFriends(self):
        return self.friends.all()
    getAllFriends.short_description = 'Friends'

    def getFriendsActivate(self):
        return self.friends.all().filter(active=True)
    getAllFriends.short_description = 'Friends Act'

    def getFriendsDesactive(self):
        return self.friends.all().filter(active=False)
    getAllFriends.short_description = 'Friends DesAct'

    def getNumFriendsActive(self):
        return self.friends.all().filter(active=True).count()
    getNumFriendsActive.short_description = 'Num Friends Act'

    def getNumFriendsDesactive(self):
        return self.friends.all().filter(active=False).count()
    getNumFriendsDesactive.short_description = 'Num Friends DesAct'

    def getNumAllFriends(self):
        return self.friends.all().count()
    getNumAllFriends.short_description = 'Num Friends'

    def getDevices(self):
        return self.device.all()
    getDevices.short_description = 'Devices'

    def getNumDevices(self):
        return self.device.all().count()
    getNumDevices.short_description = 'Num devices'

    def getGroups(self):
        return self.group_set.all()
    getGroups.short_description = 'Groups'

    def getNumGroups(self):
        return self.group_set.all().count()
    getNumGroups.short_description = 'Num groups'
