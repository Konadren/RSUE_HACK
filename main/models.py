from django.db import models

class Date(models.Model):
    start_date = models.DateField('Start')
    end_date = models.DateField('End')

    class Meta:
        db_table = 'main_date'

class Persons(models.Model):
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

    class Meta:
        db_table = 'Persons'

class BurnedPeople(models.Model):
    PersonId = models.CharField(max_length=50, default='1')
    Commit = models.CharField(max_length=50, default='1')
    Task = models.CharField(max_length=50, default='1')
    Message = models.CharField(max_length=50, default='1')
    Crunch = models.CharField(max_length=50, default='1')
    BurnChance = models.CharField(max_length=50, default='1')
    Name = models.CharField(max_length=50, default='1')
    LastName = models.CharField(max_length=50, default='1')

    class Meta:
        db_table = 'BurnedPeople'




