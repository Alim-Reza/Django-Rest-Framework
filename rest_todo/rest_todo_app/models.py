from django.db import models
from django.utils import timezone

# Create your models here.
class  Employer(models.Model):
    name = models.CharField(max_length=100)
    designation =models.CharField(max_length=100, null=True)
    salary = models.IntegerField(null=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    supervisor = models.CharField(max_length=100, null=True)


class Companies(models.Model):
    name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100, null=True)
    number_of_employees = models.IntegerField(null = True)
    founding_date = models.DateTimeField(auto_now_add = True)

