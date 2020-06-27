# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:18:25 2020

@author: Aryaman
"""

stan=float(input("Enter the step angle in degrees"))
dist= float(input("Enter distance to be covered in cm"))
dia=float(input("Enter wheel diameter in cm"))

circum= dia*3.14

distep=stan/360*circum

totste=dist/distep

print ("The number of steps to cover " + str(dist) + (" cm is " + str(totste) + (" Steps")))

