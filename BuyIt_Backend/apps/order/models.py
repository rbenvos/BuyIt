import datetime
from django.db import models
from apps.product.models import Item

"""
Clase listado
"""


class Order(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    items = models.ManyToManyField(Item, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " " + self.name

    def order_products(self):
        return self.items.all()
    order_products.short_description = "Products"

    def order_num_products(self):
        return self.items.all().count()
    order_num_products.short_description = "Num Products"

    def get_groups(self):
        return self.group_set.all()
    get_groups.short_description = 'Groups'


class OrderSetting(models.Model):
    name = models.CharField(max_length=200)
