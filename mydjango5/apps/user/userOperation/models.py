# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['username']

    def __unicode__(self):
        return self.username

class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=30)
    companyAdd = models.CharField(max_length=50)

    def __unicode__(self):
        return self.companyName


class Staff(models.Model):
    staffId = models.AutoField(primary_key=True)
    staffName = models.CharField(max_length=30)
    staffSalary = models.IntegerField()
    staCompany = models.ForeignKey(Company)

    def __unicode__(self):
        return self.staffName


