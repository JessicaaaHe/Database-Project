# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Project(models.Model):
    pname = models.CharField(max_length = 50, verbose_name = u"project name")
    pdescription = models.CharField(max_length = 300, verbose_name = u"project description")
    tag = models.CharField(max_length = 20, verbose_name = u"project category description")
    mingoal = models.FloatField(verbose_name = u"min funds needed")
    maxgoal = models.FloatField(verbose_name = u"max funds needed")
    actualamount = models.FloatField(verbose_name = u"actual funds collected")
    posttime = models.DateTimeField(default = datetime.now, verbose_name = u"post date of request")
    endtime = models.DateTimeField(verbose_name=u"end date of request")
    completetime = models.DateTimeField(default = datetime.now, verbose_name=u"complete time of request")
    pstate = models.CharField(choices = (("live", "live"),("canceled", "canceled"), ("suspend", "suspend"), ("failed", "failed"), ("successful", "successful")), max_length = 10, verbose_name = u"project state")

    likesnum = models.IntegerField(default = 0, verbose_name = u"likes number")
    image = models.ImageField(upload_to="Project/%Y/%m", verbose_name = u"project image", max_length=100)

    class Meta:
        verbose_name = u"project"
        verbose_name_plural = verbose_name


class Sample(models.Model):
    pname = models.ForeignKey(Project, verbose_name = u"project name")
    stitle = models.CharField(max_length = 50, verbose_name = u"title of sample")
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u"add time")
    download = models.FileField(upload_to = "Project/resource/%Y/%m", verbose_name = u"sample file", max_length = 100)

    class Meta:
        verbose_name = u"sample"
        verbose_name_plural = verbose_name


