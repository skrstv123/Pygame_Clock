import pygame
import datetime
import math
from settings import *
from os import path
from drawToScreen import *
from clocks import *

#initializing pygame
pygame.init()

#initializing the display
pygame.display.set_caption("sfa")
scr=pygame.display.set_mode((WIDTH, HEIGHT))
timer=pygame.time.Clock()

#game variables
img_dir = path.join(path.dirname(__file__),"img")
icon_img = path.join(img_dir,"icon_2.jpeg")
game_icon = pygame.image.load(icon_img) #loading the image into pygame
pygame.display.set_icon(game_icon) #setting the image as the icon
clk = 1 #number of the clock displayed on the screen

def clockk():
    clk = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_DOWN:
                    clk = (clk+1)%CLOCK_NUMBER
                if event.key == pygame.K_UP:
                    clk = (clk-1)%CLOCK_NUMBER

        drawClock(scr,clk)
        pygame.display.update()
        timer.tick(10)

clockk()
