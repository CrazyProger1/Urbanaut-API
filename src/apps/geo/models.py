from cities_light.abstract_models import (
    AbstractCity,
    AbstractRegion,
    AbstractCountry,
    AbstractSubRegion,
)
from cities_light.receivers import connect_default_signals
from django.db import models
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
    pass


connect_default_signals(City)


class SubRegion(AbstractSubRegion):
    pass


connect_default_signals(SubRegion)
