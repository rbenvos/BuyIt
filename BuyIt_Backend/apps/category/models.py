import datetime
from django.db import models

"""
Clase categoria
"""


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    subcategory = models.FloatField("Subcategory", blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_subcategories(self):
        return self.subcategory.all()
    get_subcategories.short_description = 'Subcategories'

"""
Clase subcategoria
"""


class Subcategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
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
        return super(Subcategory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
