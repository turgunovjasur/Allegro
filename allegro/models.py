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




# allegro_app/models.py
class Message(models.Model):
    jonatuvchi = models.ForeignKey(Shaxs, on_delete=models.CASCADE, related_name='sent_messages')
    oluvchi = models.ForeignKey(Shaxs, on_delete=models.CASCADE, related_name='received_messages')
    mavzu = models.CharField(max_length=200)
    tarkib = models.TextField()
    qoshilgan_vaqt = models.DateTimeField(auto_now_add=True)


