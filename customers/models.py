from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.company_name
