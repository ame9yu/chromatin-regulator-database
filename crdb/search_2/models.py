# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class chromatin_regulators(models.Model):
	ensembl_id = models.CharField(max_length=1000)
