from django.db import models

class employees(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

def __str__(self):
    return self.fname