from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _


class Weekday(models.IntegerChoices):
    MONDAY = 0, _("Monday")
    TUESDAY = 1, _("Tuesday")
    WEDNESDAY = 2, _("Wednesday")
    THURSDAY = 3, _("Thursday")
    FRIDAY = 4, _("Friday")
    SATURDAY = 5, _("Saturday")
    SUNDAY = 6, _("Sunday")


class CommissionPercentField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.max_digits = 4
        self.decimal_places = 2
        self.validators = [
            MinValueValidator(Decimal("0.00")),
            MaxValueValidator(Decimal("10.00")),
        ]
