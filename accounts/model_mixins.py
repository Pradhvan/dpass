from django.db import models


class AddressModelMixin(models.Model):
    name = models.CharField("Full name", max_length=100)
    address1 = models.CharField("Address line 1", max_length=500)
    address2 = models.CharField("Address line 2", max_length=500, blank=True, null=True)
    pin_code = models.CharField("Pin Code", max_length=12)
    city = models.CharField("City", max_length=50)

    class Meta:
        abstract = True
