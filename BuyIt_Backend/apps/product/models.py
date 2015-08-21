import datetime
from django.db import models


"""
Clase elemento
"""


class Item(models.Model):
    active = models.BooleanField(default=True)
    purchased = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)
    product = models.ForeignKey("Product")
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    def getOrder(self):
        return self.order_set.all()
    getOrder.short_description = 'Order'


"""
Clase producto
"""


class Product(models.Model):

    UNITS = (
        ('kg', 'Kilogramos'),
        ('l', 'Litros')
    )

    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    measure = models.CharField(max_length=3, choices=UNITS, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
