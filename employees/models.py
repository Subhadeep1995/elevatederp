from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
