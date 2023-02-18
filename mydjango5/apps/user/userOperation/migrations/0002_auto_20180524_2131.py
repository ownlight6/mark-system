# -*- coding: utf-8 -*-
# Generated by Django file and filefolder.11.11 on 2018-05-24 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userOperation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyId', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=30)),
                ('companyAdd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffId', models.AutoField(primary_key=True, serialize=False)),
                ('staffName', models.CharField(max_length=30)),
                ('staffSalary', models.IntegerField()),
                ('staCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userOperation.Company')),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
    ]
