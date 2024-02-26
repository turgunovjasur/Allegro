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
        return f"{self.Ism} {self.Familiya}"


class Xabarlar(models.Model):
    xabar_turi_CHOICES = [
        ('ariza', 'Ariza'),
        ('tatil', 'Tatil'),
    ]
    xabar_turi = models.CharField(max_length=50, choices=xabar_turi_CHOICES)

    def __str__(self):
        return self.xabar_turi


class Ariza(models.Model):
    xabar = models.ForeignKey(Xabarlar, related_name='arizalar', on_delete=models.CASCADE)
    shaxs = models.ForeignKey(Shaxs, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ariza: {self.Shaxs.Ism} {self.Shaxs.Familiya}"






