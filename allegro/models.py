from django.db import models


class Bolim(models.Model):
    Nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.Nomi


class Shaxsiy_kabinet(models.Model):
    Ism = models.CharField(null=False, blank=False, max_length=10)
    Familiya = models.CharField(null=False, blank=False, max_length=100)
    Bolim = models.ForeignKey(Bolim, null=True, on_delete=models.SET_NULL)
    tel = models.CharField(null=False, blank=False, max_length=100, unique=True)
    address = models.CharField(max_length=255)
    Qoshilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Ism} {self.Familiya}"



