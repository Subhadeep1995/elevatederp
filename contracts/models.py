from django.db import models
from customers.models import Customer

PROPOSAL_STATUS = [
    ('P', 'Pending'),
    ('A', 'Apporved'),
    ('R', 'Rejected'),
]

CONTRACT_STATUS = [
    ('P', 'Pending'),
    ('C', 'Completed'),
]

PAYMENT_MODE = [
    ('M', 'Monthly'),
    ('B', 'Biannual'),
    ('A', 'Annual'),
]


class Proposal(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE,)
    proposal_url = models.CharField(max_length=200)
    status = models.CharField(
        max_length=1, choices=PROPOSAL_STATUS, default='P')

    def __str__(self):
        return self.customer


class Contract(models.Model):
    contract_status = models.CharField(
        max_length=1, choices=CONTRACT_STATUS, default='P')
    proposed_amount = models.DecimalField(max_digits=20, decimal_places=2)
    agreed_amount = models.DecimalField(max_digits=20, decimal_places=2)
    round_area = models.ForeignKey('Area', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contract_url = models.CharField(max_length=200)
    customer = models.OneToOneField(
        'customers.Customer', on_delete=models.CASCADE,)
    payment_mode = models.CharField(
        max_length=1, choices=PAYMENT_MODE, default='M')

    def __str__(self):
        return self.customer.company_name


class Area(models.Model):
    area_name = models.CharField(max_length=20, default='Here')
    area_code = models.CharField(max_length=10)
    roundsman = models.ForeignKey(
        'employees.Employee', on_delete=models.CASCADE,)

    def __str__(self):
        return self.area_name
