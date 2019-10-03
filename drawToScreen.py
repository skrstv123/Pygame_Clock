import pygame
import datetime
import math

def drawPoints(screen,da,col,radd):
	for _ in range(0,367,da):
		_=math.radians(_)
		a,b=int(250+160*math.sin(_)),int(90+160*(1-math.cos(_))) #for the location of the smaller dots
		pygame.draw.circle(screen,col,(a,b),radd)
		if _%math.radians(90)==0:
			a,b=int(250+150*math.sin(_)),int(100+150*(1-math.cos(_)))
			pygame.draw.circle(screen,(40,0,255),(a,b),6)

def fireHand(screen,rsycth):
	r,s,y,c,th=rsycth[0],rsycth[1],rsycth[2],rsycth[3],rsycth[4]
	a,b=250+r*math.sin(s),y+r*(1-math.cos(s))
	pygame.draw.lines(screen,c,True,[[250,250],[a,b]],th)
