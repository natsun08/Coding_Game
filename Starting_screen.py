import pygame
from sys import exit
#MANDATORY
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Platform')
clock = pygame.time.Clock()

#VARIABLE
font_text_type = pygame.font.Font(None, 100)
font_start_type = pygame.font.Font(None, 50)
scene = "starting"

#OBJECT
sky_surface = pygame.Surface((1000, 600))
sky_surface.fill("cyan")
ingame_surface= pygame.Surface((800, 500))
ingame_surface.fill("Brown")
function_surface= pygame.Surface((200, 600))
function_surface.fill("Gray")
activate_surface= pygame.Surface((800, 100))
activate_surface.fill("White")
activate_surface.set_alpha(80)
text_surface = font_text_type.render ("Nyanja", False, "Brown")
starting = font_start_type.render ("Click anywhere to start", False, "Purple")
text_surface = font_text_type.render ("Well come to our game", False, "Brown")

#RECTANGLE
text_surface_rect = text_surface.get_rect(center = (500, 250))
starting_rect = starting.get_rect(center = (500, 400))


while scene == "starting":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            scene = "scene1"
    if scene != "starting":
        break
    screen.blit(sky_surface, (0,0))
    screen.blit(text_surface, text_surface_rect)
    screen.blit(starting, starting_rect)
    

    pygame.display.update()
    clock.tick(60)



while scene == "scene1":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(ingame_surface, (0,0))
    screen.blit(function_surface, (800,0))
    screen.blit(activate_surface, (0,500))
    
    pygame.display.update()
    clock.tick(60)