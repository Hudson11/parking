from django.db import models
from django.core.validators import RegexValidator
from re import compile

plate_format = compile("^[a-zA-Z]{3}-[0-9]{4}$")


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Parking(Base):
    plate = models.CharField(max_length=8, validators=[
        RegexValidator(
            regex=plate_format,
            message='This format is not valid, try using the standard AAA-9999',
            code='invalid_plate'
        )
    ])
    check_out = models.BooleanField(default=False, editable=False)
    pay = models.BooleanField(default=False, editable=False)
    minutes = models.CharField(default='', max_length=50, editable=False)
    reservation = models.CharField(default='', max_length=50, editable=False)

    class Meta:
        verbose_name = 'Parking'
        verbose_name_plural = 'Parking`s'
        ordering = ['id']

    def __str__(self):
        return f'plate {self.plate} Check-out {self.check_out} pay: {self.pay} reservation: {self.reservation}'
