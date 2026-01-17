from cities_light.abstract_models import (
    AbstractCity,
    AbstractRegion,
    AbstractCountry,
    AbstractSubRegion,
)
from cities_light.receivers import connect_default_signals
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Country(AbstractCountry):
    is_active = models.BooleanField(
        default=True,
        blank=False,
        null=False,
        verbose_name=_("is active"),
        help_text=_("Country is supported"),
    )


connect_default_signals(Country)


class Region(AbstractRegion):
    pass


connect_default_signals(Region)


class City(AbstractCity):
    point = models.PointField(
        verbose_name=_("point"),
        help_text=_("Point of the city."),
        null=True,
        blank=True,
    )


connect_default_signals(City)


class SubRegion(AbstractSubRegion):
    pass


connect_default_signals(SubRegion)


class Address(models.Model):
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        verbose_name=_("country"),
        null=False,
        blank=False,
    )
    region = models.ForeignKey(
        to=Region,
        on_delete=models.CASCADE,
        verbose_name=_("region"),
        null=True,
        blank=True,
    )
    subregion = models.ForeignKey(
        to=SubRegion,
        on_delete=models.CASCADE,
        verbose_name=_("subregion"),
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE,
        verbose_name=_("city"),
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name=_("address"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(
            self.text or self.city or self.subregion or self.region or self.country
        )
