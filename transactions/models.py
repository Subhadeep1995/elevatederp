from django.db import models
from contracts.models import Contract

PAYMENT_STATUS = [
    ('D', 'Due'),
    ('O', 'Overdue'),
    ('C', 'Complete'),
]


class Transaction(models.Model):
    contract_id = models.OneToOneField(
        Contract, related_name='contract_id', on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    amount_due = models.OneToOneField(
        Contract, related_name="amount_due", on_delete=models.CASCADE)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default='D')
    payment_completion_date = models.DateTimeField(
        auto_now=True, editable=False)
