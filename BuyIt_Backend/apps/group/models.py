import datetime
from django.db import models
from apps.order.models import Order
from apps.user.models import User

"""
Clase grupo
"""

class Group(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    orders = models.ManyToManyField(Order,blank=True)
    #avatar = models.ImageField(blank=True)
    users = models.ManyToManyField(User,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Group, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " " + self.name

    def groupUsers(self):
        return self.users.all()
    groupUsers.short_description = "Users"

    def groupOrders(self):
        return self.orders.all()
    groupOrders.short_description = "Orders"