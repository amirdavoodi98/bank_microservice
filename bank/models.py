from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    manager_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    manager_id = models.IntegerField(default=0)