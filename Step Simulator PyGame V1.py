# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:13:30 2020

@author: Abhijit
"""


import pygame as pg
from time import sleep as s
import rotateImage as rotator

# Pygame Initisalise

pg.init()

#Variables

w=1024
h=1024
angle=0
evesta="work"
ste=0
#Screen

screen=pg.display.set_mode((w,h))

#Inputs

stan=float(input("Enter the step angle in degrees"))
dist= float(input("Enter distance to be covered in cm"))
dia=float(input("Enter wheel diameter in cm"))

#Caption

pg.display.set_caption("Step Simulator")

#Image Load

backimg=pg.image.load("Images/Blue Background.png")

screen.blit(backimg,(0,0))

#Calculation of steps

circum= dia*3.14

distep=stan/360*circum

totste=dist/distep


# Rotating Image Load

roimg=pg.image.load("Images/Circle Rotator Image.jpg")


#Text Print

font=pg.font.SysFont("Ariel", 40, 4)
text=font.render("The Number of Steps are- " + str(totste), True, (255,255,255))

screen.blit(text,(0,700))

while True:
    pg.display.update()
    
    while ste<=totste:
        rotator.blitRotate(screen, roimg, (100,100), angle)
    
        angle=angle+stan
    
        s(1)
        
        ste=ste+1
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            evesta="quit"
            break
    if evesta=="quit":
        break