import datetime
from django.db import models


"""
Clase elemento
"""


class Item(models.Model):
    active = models.BooleanField(default=True)
    purchased = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)
    product = models.ForeignKey("Product", blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    def get_order(self):
        return self.order_set.all()
    get_order.short_description = 'Order'


"""
Clase producto
"""


class Product(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    quantity = models.ForeignKey('Quantity', blank=True, null=True)
    measure = models.ForeignKey('Measure', blank=True, null=True)
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


class Quantity(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Quantity, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Measure, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

