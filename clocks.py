import pygame
from drawToScreen import *
from clockMath import *
from settings import *

def drawClock(screen, n):
    if n==0:
        drawClock0(screen)
    elif n==1:
        drawClock1(screen)

def drawClock0(screen):
    screen.fill((0,0,0))

    pygame.draw.circle(screen,(80,0,90),(250,250),190,8)
    drawPoints(screen,6,(160,0,200),2)
    drawPoints(screen,30,(200,0,160),5)

    t=list(map(int,hms()))
    h,m,s=t[0],t[1],t[2]

    angh,angm,angs=math.radians((h/12)*360),math.radians((m/60)*360),math.radians((s/60)*360)
    if m>5:
        angh+=math.radians(30*(m/60))
    fireHand(screen,[85,angh,165,(255,255,255),4])
    fireHand(screen,[150,angm,100,(255,0,0),3])

    fireHand(screen,[170,angs,80,(0,255,0),2])
    pygame.draw.circle(screen,(0,255,0),(250,250),11)

def drawClock1(screen):
    screen.fill(WHITE)
    pygame.draw.circle(screen,BLACK,(250,250),190,8)
    drawPoints(screen,6,BLACK,2)
    drawPoints(screen,30,BLACK,5)

    t=list(map(int,hms()))
    h,m,s=t[0],t[1],t[2]

    angh,angm,angs=math.radians((h/12)*360),math.radians((m/60)*360),math.radians((s/60)*360)
    if m>5:
        angh+=math.radians(30*(m/60))
    fireHand(screen,[85,angh,165,BLACK,4])
    fireHand(screen,[150,angm,100,(255,0,0),3])

    fireHand(screen,[170,angs,80,BLACK,2])
    pygame.draw.circle(screen,BLACK,(250,250),11)
