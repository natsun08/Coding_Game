import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Test Teaching Coding")
bg = pygame.image.load("nen_anh_dao.jpg")
bg = pygame.transform.scale(bg,(1280,720))

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

#TEXT
font1 = pygame.font.Font("freesansbold.ttf", 35)
text1 = font1.render("This is a text about PyGame", True, YELLOW, RED)

while True:
    DISPLAYSURF.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()