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
    nomi = models.CharField(max_length=50, null=True)
    shablon = models.TextField(null=True)

    def __str__(self):
        return self.nomi


class Ariza(models.Model):
    xabar = models.ForeignKey(Xabarlar, related_name='xabarlar', on_delete=models.CASCADE)
    shaxs = models.ForeignKey(Shaxs, on_delete=models.CASCADE)
    matn = models.TextField(null=True)
