# -*- coding: utf-8 -*-
# Generated by Django file and filefolder.11.11 on 2018-05-08 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=30)),
                ('jobsalary', models.IntegerField()),
            ],
        ),
    ]
