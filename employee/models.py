from django.db import models

from bank.models import Branch

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='employees')