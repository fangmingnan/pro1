# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

# Create your models here.

class LiuYanKu(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

