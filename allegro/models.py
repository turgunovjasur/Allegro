from django.db import models


class Profile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=10)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    phone_number = models.CharField(null=False, blank=False, max_length=100, unique=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
