import pygame
from pygame.locals import *

WINDOWWIDTH = 1280 # Chiều dài cửa sổ
WINDOWHEIGHT = 720 # Chiều cao cửa sổ


pygame.init()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption("Mini Game Test")

#FPS
FPS = 90
fpsClock = pygame.time.Clock()

#Background
bg = pygame.image.load("bridge.jpg")

    

#Car
class Car():
    def __init__(self):
        self.x = 0 # Vị trí của xe

        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = pygame.image.load('car.png')
    
    def draw(self): # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, 380))

    def update(self): # Hàm dùng để thay đổi vị trí xe
        self.x += 2
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100

car = Car()

while True:
    bg = pygame.transform.scale(bg,(1280,720))
    DISPLAYSURF.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    car.draw()
    car.update()

    pygame.display.update()
    fpsClock.tick(FPS)

    
    

