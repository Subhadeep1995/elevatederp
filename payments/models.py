from django.db import models
from contracts.models import Contract
from decimal import Decimal


PAYMENT_STATUS = [
    ('D', 'Due'),
    ('O', 'Overdue'),
    ('C', 'Complete'),
]


class Payment(models.Model):
    contract = models.ForeignKey(
        'contracts.Contract', on_delete=models.CASCADE,)
    due_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default='D')
    amount_due = models.DecimalField(max_digits=20, decimal_places=2)
    amount_paid = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    outstanding = models.DecimalField(max_digits=20, decimal_places=2)
    remarks = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.status
