from django.db import models

from bank.models import Bank, Branch

class Account(models.Model):
    account_no = models.CharField(max_length=10, primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
