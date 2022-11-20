from django.db import models
from django.utils.translation import gettext_lazy as translate

from .meta import COUNTRIES


class Address(models.Model):
    address = models.CharField(
        translate("Address"),
        max_length=255,
        blank=True,
        default=""
    )
    address2 = models.CharField(
        translate("Address2"),
        max_length=55,
        blank=True,
        default=""
    )
    city = models.CharField(
        translate("City"),
        max_length=255,
        blank=True,
        default=""
    )
    zipcode = models.CharField(
        translate("Post/Zip-code"),
        max_length=64,
        blank=True,
        default=""
    )
    state = models.CharField(
        translate("State"),
        max_length=255,
        blank=True,
        default=""
    )
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, default="")

    def __str__(self):
        return self.city if self.city else ""


class Organisation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.ForeignKey(Address, blank=True, on_delete=models.CASCADE)
    user_limit = models.IntegerField(default=5)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)
