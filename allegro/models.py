from django.db import models


class Bolim(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Shaxs(models.Model):
    ism = models.CharField(null=False, blank=False, max_length=10)
    familiya = models.CharField(null=False, blank=False, max_length=100)
    bolim = models.ForeignKey(Bolim, null=True, on_delete=models.SET_NULL)
    tel = models.CharField(null=False, blank=False, max_length=100, unique=True)
    address = models.CharField(max_length=255)
    qoshilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Xabarlar(models.Model):
    xabar_turi_CHOICES = [
        ('ariza', 'Ariza'),
        ('tatil', 'Tatil')
    ]
    xabar_turi = models.CharField(max_length=50, choices=xabar_turi_CHOICES)

    def __str__(self):
        return self.xabar_turi


class Ariza(models.Model):
    xabar = models.ForeignKey(Xabarlar, related_name='xabarlar', on_delete=models.CASCADE)
    shaxs = models.ForeignKey(Shaxs, on_delete=models.CASCADE)

    def __str__(self):
        return f"Men: {self.shaxs.ism} {self.shaxs.familiya}ning birinchi arizam!"


##########


from django.db import models
from shared.django.model import BaseModel
from django.db.models import Min

# Project
from automobile.models import Car


class PositionCategory(BaseModel):
    # relations
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    engine = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    available_volume = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    transmission_box = models.CharField(max_length=255)
    overclocking_time = models.FloatField()
    max_speed = models.IntegerField()

    # security
    lockingRearWheelDifferential = models.BooleanField(default=False)
    automaticAutoHold = models.BooleanField(default=False)
    childSeatLock = models.BooleanField(default=False)

    # exterior
    led_headlight = models.CharField(max_length=255)
    full_weight = models.FloatField()
    empty_weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    seats_count = models.IntegerField()

    def __str__(self):
        return str(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.cost and self.car:
            min_cost = PositionCategory.objects.aggregate(Min('cost'))['cost__min']
            if min_cost is None:
                min_cost = 0
            if self.cost < min_cost:
                min_cost = self.cost
            car = Car.objects.get(id=self.car.id)
            car.cost_from = min_cost
            car.save()
        super().save(force_insert, force_update, using, update_fields)

from django.db import models
from shared.django.model import BaseModel
from colorfield.fields import ColorField


class Car(BaseModel):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red")
    ]
    title = models.CharField(max_length=255)
    cost_from = models.FloatField()
    color = ColorField(choices=COLOR_CHOICES)
    about = models.TextField()
    internal_possibility = models.TextField()
    appearance = models.TextField()

    internal_photo = models.ImageField()
    external_photo = models.ImageField()
    side_photo = models.ImageField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)