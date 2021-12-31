import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption("Test Teaching Coding")

#COLOR
GRAY     = (100,100,100)
NAVIBLUE = (60,60,100)
WHITE    = (255,255,255)
RED      = (255,0,0)
GREEN    = (0,255,0)
BLUE     = (0,0,255)
YELLOW   = (255,255,0)
ORAGNE   = (255,128,0)
PURPLE   = (255,0,255)
CYAN     = (0,255,255)

#RectObject
MyRect = pygame.Rect(50,50,100,100)
print(MyRect.centerx)

while True:
    pygame.draw.rect(DISPLAYSURF, BLUE, (50,50,100,100))
    pygame.draw.circle(DISPLAYSURF, GREEN, (250,200),50)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()