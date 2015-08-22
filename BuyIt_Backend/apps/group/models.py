import datetime
from django.db import models
from apps.order.models import Order

"""
Clase grupo
"""


class Group(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    orders = models.ManyToManyField(Order, blank=True)
    settings = models.ManyToManyField("GroupSetting", blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Group, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " " + self.name

    def group_users(self):
        return self.member_set.all()
    group_users.short_description = "Users"

    def group_orders(self):
        return self.orders.all()
    group_orders.short_description = "Orders"


class GroupSetting(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.id) + ' ' + self.name
