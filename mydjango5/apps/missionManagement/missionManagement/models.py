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

class Job(models.Model):
    jobname = models.CharField(max_length=30)
    jobsalary = models.IntegerField()

    def __unicode__(self):
        return self.jobname