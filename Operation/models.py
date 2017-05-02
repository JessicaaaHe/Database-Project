# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from User.models import UserProfile
from Project.models import Project
from User.models import CreditCard

# Create your models here.


class ProjectComment(models.Model):
    logname = models.ForeignKey(UserProfile, verbose_name = u"user's logname")
    pname = models.ForeignKey(Project, verbose_name = u"project name")
    comments = models.CharField(max_length = 200, verbose_name = u"comments")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"projectcomment"
        verbose_name_plural = verbose_name


class ProjectRate(models.Model):
    logname = models.ForeignKey(UserProfile, verbose_name = u"user's logname")
    pname = models.ForeignKey(Project, verbose_name = u"project name")
    ratelevel = models.IntegerField(choices= ((1, "1 star"), (2, "2 stars"),(3, "3 stars"), (4, "4 stars"), (5, "5 stars")), default = 5, verbose_name = "ratelevel")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"projectrate"
        verbose_name_plural = verbose_name


class UserFavourite(models.Model):
    logname = models.ForeignKey(UserProfile, verbose_name=u"user's logname")
    fav_id = models.IntegerField(default = 0, verbose_name= "id")
    fav_type = models.IntegerField(choices= ((1, "user"), (2, "project")), default = 1, verbose_name = "favourite type")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"favourite"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default = 0, verbose_name= "receive user")
    message = models.CharField(max_length = 500, verbose_name= "message content")
    has_read =models.BooleanField(default = False, verbose_name= "if read")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"user message"
        verbose_name_plural = verbose_name


class UserProject(models.Model):
    logname = models.ForeignKey(UserProfile, verbose_name=u"user's logname")
    pname = models.ForeignKey(Project, verbose_name=u"project name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"user's project"
        verbose_name_plural = verbose_name


class Charge(models.Model):
    logname = models.ForeignKey(UserProfile, verbose_name=u"user's logname")
    pname = models.ForeignKey(Project, verbose_name=u"project name")
    creditnum = models.ForeignKey(CreditCard, verbose_name=u"creditcard number")
    charamount = models.FloatField(verbose_name = u"amount charged")
    charstate = models.CharField(choices=(("successful", "successful"), ("pending", "pending"), ("failed", "failed")), max_length=10, verbose_name=u"charge state")
    chartime = models.DateTimeField(default=datetime.now, verbose_name=u"charge time")

    class Meta:
        verbose_name = u"charge"
        verbose_name_plural = verbose_name







