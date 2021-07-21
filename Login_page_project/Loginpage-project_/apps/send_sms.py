#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:56:17 2020

@author: jothishr
"""


import requests
import random

class Sms_send:

	def __init__(self):
		pass

	def Gen_random_num(self):
		try:
			otp = random.randint(100000, 999999)
			return otp
		except Exception as e:
			print(e)

	def send(self):
		pass
		
	
ob = Sms_send()
ob.Gen_random_num()