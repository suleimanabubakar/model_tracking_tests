from django.db import models
from simple_history.models import HistoricalRecords
from simple_history import register as sRegister

# Create your models here.

class Ticket(models.Model):
    name =  models.CharField(max_length=30)
    history = HistoricalRecords()

    

class Student(models.Model):
    name = models.CharField(max_length=30)


sRegister(Student)




class Teacher(models.Model):
    name = models.CharField(max_length=30)

sRegister(Teacher)