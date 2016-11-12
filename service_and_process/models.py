from django.db import models
from django.contrib.auth.models import User


class MasterAttribute(models.Model):
    """Cotton, Linen"""

    TYPE_CHOICES = ((1, 'Material'), )

    label = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)

    class Meta:
        unique_together = (("label", "type"), )


class MasterWorkable(models.Model):
    """e.g. Shirt, T. Shirt, Trousers"""

    CATEGORY_CHOICES = ((1, 'Gentlemen'),
                        (2, 'Women'))

    label = models.TextField()
    category = models.IntegerField(null=True, choices=CATEGORY_CHOICES)
    attribute = models.ForeignKey(MasterAttribute, blank=True, null=True)   # many if required


class MasterService(models.Model):
    """e.g. Dry Washing"""

    label = models.TextField()
    workable = models.ForeignKey(MasterWorkable)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)


class MasterProduct(models.Model):
    """Cookies"""
    UNIT_CHOICES = ((1, 'Piece'),
                    (2, 'Kg'))

    label = models.TextField()
    shelf_life_in_days = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    batch_size = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES)


class MasterProcess(models.Model):
    """e.g. Billing, Sorting, QC, Washing"""

    label = models.TextField()
    category = models.ForeignKey('people.MasterUnit')


class MappingProductServicesProcess(models.Model):

    """e.g., Cookies -- bake, Knead, etc """

    process = models.ForeignKey(MasterProcess)
    service = models.ForeignKey(MasterService, null=True)
    product = models.ForeignKey(MasterProduct, null=True)
