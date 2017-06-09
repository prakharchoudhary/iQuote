# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from .choices import CATEGORY_CHOICES 
# Create your models here.

class Quote(models.Model):

	created = models.DateTimeField(auto_now_add = True)
	quote = models.CharField(max_length=140)
	category = models.CharField(choices=CATEGORY_CHOICES, default='Happy', max_length=100)

