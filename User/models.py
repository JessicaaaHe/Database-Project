# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.


class UserProfile(AbstractUser):
    logname = models.CharField(max_length = 30, verbose_name = "user's log in name")
    hometown = models.CharField(max_length = 50, null = True, blank = True, default = u"")
    interest = models.CharField(max_length = 100, null = True, blank = True, default = u"")
    image = models.ImageField(upload_to = "image/%Y/%m", default = u"image/default.png", max_length = 100)
    follownum = models.IntegerField(default = 0, verbose_name = u"follow number")

    class Meta:
        verbose_name = u"user's information"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length = 20, verbose_name = u"verified code")
    email = models.EmailField(max_length = 50, verbose_name = u"email")
    send_type = models.CharField(choices = (("register", u"register"),("forget", u"find back password")), max_length = 10)
    send_time = models.DateTimeField(default = datetime.now)

    class Meta:
        verbose_name = u"email verify code"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name = u"banner image", max_length=100)
    url = models.URLField(max_length = 200, verbose_name = u"url")
    index = models.IntegerField(default = 100, verbose_name = u"sequence")
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u"add time")

    class Meta:
        verbose_name = u"banner image"
        verbose_name_plural = verbose_name

class CreditCard(models.Model):
    creditnum = models.CharField(max_length = 16, verbose_name = "card number")
    logname = models.ForeignKey(UserProfile, verbose_name=u"user's logname")
    realname = models.CharField(max_length = 30,verbose_name = "card holder's name")
    securitycode = models.CharField(max_length = 3, verbose_name = "securitycode")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"credit card"
        verbose_name_plural = verbose_name