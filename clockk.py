"""
	pygame Clock, by skrstv123 (Shekhar Srivastava)
	<fun with maths>
"""



import pygame
import datetime
import math
pygame.init()

pygame.display.set_caption("sfa")
scr=pygame.display.set_mode((500,500))
timer=pygame.time.Clock()

#x,y,a,b=250,250,300,100

def hms():
	x=str(datetime.datetime.now())
	x=x.split(" ")
	x=x[1]
	x=x.split('.')
	x=x[0]
	x=x.split(':')
	return x
	
def fireHand(rsycth): 
	r,s,y,c,th=rsycth[0],rsycth[1],rsycth[2],rsycth[3],rsycth[4]
	a,b=250+r*math.sin(s),y+r*(1-math.cos(s))
	pygame.draw.lines(scr,c,True,[[250,250],[a,b]],th)
	
def drawPoints(da,col,radd):
	for _ in range(0,367,da):
		_=math.radians(_)
		a,b=int(250+160*math.sin(_)),int(90+160*(1-math.cos(_)))
		pygame.draw.circle(scr,col,(a,b),radd)
		if _%math.radians(90)==0:
			a,b=int(250+150*math.sin(_)),int(100+150*(1-math.cos(_)))
			pygame.draw.circle(scr,(40,0,255),(a,b),6)
	
def clockk():

	#ra=240
	#s=1
	#x,y,a,b=250,250,250,250
	#l=67
	while True:
		for ev in pygame.event.get():
			if ev.type==pygame.QUIT:
				pygame.quit()
				quit()
		scr.fill((0,0,0))
		pygame.draw.circle(scr,(80,0,90),(250,250),190,8)
		#pygame.draw.lines(scr,(255,0,0),True,[[x,y],[a,b]],4)
		
		
		
		
		drawPoints(6,(160,0,200),2)
		drawPoints(30,(200,0,160),5)
		
		
		
		t=list(map(int,hms()))
		h,m,s=t[0],t[1],t[2]
		
		angh,angm,angs=math.radians((h/12)*360),math.radians((m/60)*360),math.radians((s/60)*360)
		if m>5:
			angh+=math.radians(30*(m/60))
		fireHand([85,angh,165,(255,255,255),4])
		fireHand([150,angm,100,(255,0,0),3])
		
		fireHand([170,angs,80,(0,255,0),2])
		pygame.draw.circle(scr,(0,255,0),(250,250),11)
		#print(h,m,s)
		
		
		
		
		"""a+=2
		b=250-s*(a-250)
		if int(((a-x)**2+(y-b)**2)**0.5)>=l:
			x+=2
			y=250-s*(x-250)
		if a>590 or b<-90:
			a,b,x,y=250,250,250,250"""
		
		pygame.display.update()
		timer.tick(10)
	
	
	
clockk()	
	
	
	
	
	
	
	
	
	