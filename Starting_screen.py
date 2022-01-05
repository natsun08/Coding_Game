import pygame
from sys import exit
import Code.Library as Library
#CLASS

#MANDATORY
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Platform')
clock = pygame.time.Clock()

#VARIABLE
scene = "starting"
starting_screen = False

#Surface
ingame_surface= pygame.Surface((800, 500))
ingame_surface.fill("Brown")
function_surface= pygame.Surface((200, 600))
function_surface.fill("Gray")
activate_surface= pygame.Surface((800, 100))
activate_surface.fill("White")
activate_surface.set_alpha(80)

#Sprite
sky_surface = Library.ENVIROMENT("Game Asset\Sky.png", 10, "topleft", 0, 0)
cloud_1 = Library.ENVIROMENT("Game Asset\Cloud1.png", 5, "topleft" , 80, 150)
cloud_2 = Library.ENVIROMENT("Game Asset\cloud2.png", 4, "topleft" ,600, 100)
cloud_3 = Library.ENVIROMENT("Game Asset\cloud2.png", 6, "topleft" ,300, 50)
cloud_4 = Library.ENVIROMENT("Game Asset\Cloud1.png", 7, "topleft" , 750, 150)
Logo = Library.ENVIROMENT("Game Asset\Gamename.png", 0.75,"center" , 500, 200)
scrolls = Library.ENVIROMENT("Game Asset\starting Scroll.png", 10, "center", 500, 300)
scroll_close_brown = Library.ENVIROMENT("Game Asset\scroll_close.png", 3, "center", 500, 400)
scroll_close_blue = Library.ENVIROMENT("Game Asset\scroll_close_2.png", 1, "center", 440, 350)
scroll_close_gold = Library.ENVIROMENT("Game Asset\scroll_close_3.png", 1, "center", 420, 430)
start = Library.TEXT("Start","Game Asset\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 350 )
setting_text = Library.TEXT("Setting","Game Asset\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 430 )
#GROUP
starting_enviroment = pygame.sprite.Group()
starting_enviroment.add(sky_surface, cloud_1 , cloud_2,cloud_3, cloud_4 , Logo, scroll_close_brown)
second_scene = pygame.sprite.Group()
second_scene.add(scrolls, Logo, scroll_close_blue, start, setting_text, scroll_close_gold)

#STARTING SCREEN
while True:
    if scene == "starting":
        for event in pygame.event.get():
            Library.close_game(event.type)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #Left click 
                if scroll_close_brown.is_clicked(mouse) and not starting_screen:
                    starting_screen = True
                    break
                elif start.is_clicked(mouse) and starting_screen:
                    scene = "scene1"
                    break
                elif setting_text.is_clicked(mouse) and starting_screen:
                    scene = "setting"
                    break
        starting_enviroment.draw(screen)
        cloud_1.animate(2)
        cloud_2.animate(-2)
        cloud_3.animate(3)
        cloud_4.animate(-1)
        if starting_screen:
            second_scene.draw(screen)
            mouse = pygame.mouse.get_pos()
            if start.is_clicked(mouse):
                image, rect = start.colors("Red", "Black")
                screen.blit(image, rect)
            elif not start.is_clicked(mouse):
                image, rect = start.colors("Black","Red")
                screen.blit(image, rect)
            if setting_text.is_clicked(mouse):
                image, rect = setting_text.colors("Red", "Black")
                screen.blit(image, rect)
            elif not setting_text.is_clicked(mouse):
                image, rect = setting_text.colors("Black","Red")
                screen.blit(image, rect)
    elif scene == "scene1":
        for event in pygame.event.get():
            Library.close_game(event.type)
        screen.blit(ingame_surface, (0,0))
        screen.blit(function_surface, (800,0))
        screen.blit(activate_surface, (0,500))
    elif scene == "setting":
        for event in pygame.event.get():
            Library.close_game(event.type)
        pass
    pygame.display.update()
    clock.tick(60)