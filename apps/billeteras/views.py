# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .poloniex import poloniex


# Create your views here.
prueba = poloniex('PBU6QU8V-CET88BVI-VOOIHFDT-5CNMC7PR','34ebbae8bf11a4c759d606ce86674eac901f1f6293c14a1014abf437b33cb14e2a3a535fa84e98e83415e4870a49cb0e505cac1dbfdd8b98f2be090441021681c')
#print prueba.bar()
ticker = prueba.returnTicker()
valorEth = float(ticker['BTC_ETH']['last'])

#sw = 0
#while (sw == 0):
	#ticker = prueba.returnTicker()
	#valorEth = float(ticker['BTC_ETH']['last'])
	
	#if 0.10240000 <= valorEth <= 0.10340000:
	#	print ('Hey compra')
		
	#elif 0.11910000 <= valorEth <= 0.12100000:
	#	print ('Hey vende')
		
		
		

#print "Tenemos "+str(decoded["BTC_BCN"][0]["ETH"][0])+" Lechugas."


def index(request):
	return HttpResponse(valorEth)