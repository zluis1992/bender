# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Billetera(models.Model):
	moneda = models.CharField(max_length=50, unique = True)
	porcentaje_retiro = models.DecimalField( max_digits=3, decimal_places=2)
	cantidad = models.DecimalField(max_digits=13, decimal_places=5)
