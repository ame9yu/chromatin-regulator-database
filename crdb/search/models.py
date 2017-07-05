# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class chromatin_regulator(models.Model):
    ensembl_id = models.CharField(max_length=50)
    gene_symbol = models.CharField(max_length=10)
    function = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    genecards_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.gene_symbol
