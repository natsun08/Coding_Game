import pygame
from sys import exit
import Code.Library as Library
#MANDATORY
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Platform')
clock = pygame.time.Clock()

#VARIABLE
scene = "starting"
starting_screen = "tittlescreen"
volumn = 1.0

#MUSIC (Will be change to free music later)
pygame.mixer.music.load("Game Asset\Omoide Tsuzuri - Akatsuki.wav")
#song link: https://www.youtube.com/watch?v=yzQyzvsv2NY
pygame.mixer.music.play(-1)

#Surface
ingame_surface= pygame.Surface((800, 500))
ingame_surface.fill("Brown")
function_surface= pygame.Surface((200, 600))
function_surface.fill("Gray")
activate_surface= pygame.Surface((800, 100))
activate_surface.fill("White")
activate_surface.set_alpha(80)

#Sprite
sky_surface = Library.ENVIROMENT("Game Asset\\Sky.png", 10, "topleft", 0, 0)
cloud_1 = Library.ENVIROMENT("Game Asset\\Cloud1.png", 5, "topleft" , 80, 150)
cloud_2 = Library.ENVIROMENT("Game Asset\\cloud2.png", 4, "topleft" ,600, 100)
cloud_3 = Library.ENVIROMENT("Game Asset\\cloud2.png", 6, "topleft" ,300, 50)
cloud_4 = Library.ENVIROMENT("Game Asset\\Cloud1.png", 7, "topleft" , 750, 150)
Logo = Library.ENVIROMENT("Game Asset\\Gamename.png", 0.75,"center" , 500, 200)
scrolls = Library.ENVIROMENT("Game Asset\\starting Scroll.png", 10, "center", 500, 300)
scroll_close_brown = Library.ENVIROMENT("Game Asset\\scroll_close.png", 2.3, "center", 500, 400)
scroll_close_blue = Library.ENVIROMENT("Game Asset\\scroll_close_2.png", 1, "center", 440, 350)
scroll_close_gold = Library.ENVIROMENT("Game Asset\\scroll_close_3.png", 1, "center", 420, 430)
start = Library.TEXT("Start","Game Asset\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 350 )
setting_text = Library.TEXT("Setting","Game Asset\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 430 )
sound_icon = Library.ENVIROMENT("Game Asset\\Sound_on.png", 1.5, "center", 400, 370)
sound_status = Library.TEXT("On","Game Asset\\ninja-naruto.regular.ttf", 50, "Red", "topleft", 450, 350)
return_button = Library.ENVIROMENT("Game Asset\Return.png", 1, "topleft", 200, 450)
#GROUP
starting_enviroment = pygame.sprite.Group(sky_surface, cloud_1 , cloud_2,cloud_3, cloud_4 , Logo, scroll_close_brown)
second_scene = pygame.sprite.Group(scrolls, Logo, scroll_close_blue, start, setting_text, scroll_close_gold, return_button)
setting_screen = pygame.sprite.Group(scrolls, Logo, sound_status, sound_icon, return_button)
scene1 = pygame.sprite.Group(return_button)



#STARTING SCREEN
while True:
    if scene == "starting":
        for event in pygame.event.get():
            Library.close_game(event.type)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #Left click 
                if scroll_close_brown.is_clicked(mouse) and starting_screen == "tittlescreen":
                    starting_screen = "started or setting"
                    break
                elif starting_screen == "started or setting":
                    if start.is_clicked(mouse):
                        scene = "scene1"
                        continue
                    elif setting_text.is_clicked(mouse):
                        starting_screen = "setting"
                        break
                    elif return_button.is_clicked(mouse):
                        starting_screen = "tittlescreen"
                if starting_screen == "setting":
                    if sound_status.is_clicked(mouse) or sound_icon.is_clicked(mouse):
                        if volumn > 0.0:
                            sound_status.change_text("Off", "Black")
                            volumn = 0.0
                            sound_icon.transform_image("Game Asset\Sound_off.png", 1.5)
                        elif volumn == 0.0:
                            volumn = 1.0
                            sound_status.change_text("On", "Red")
                            sound_icon.transform_image("Game Asset\Sound_on.png", 1.5)
                        pygame.mixer.music.set_volume(volumn)
                        setting_screen.update()
                    elif return_button.is_clicked(mouse):
                        starting_screen =  "started or setting"
        if scroll_close_brown.is_clicked(mouse):
            scroll_close_brown.transform_image(new_image=None, new_scale=3)
        elif not scroll_close_brown.is_clicked(mouse):
            scroll_close_brown.transform_image(new_image=None, new_scale=2.3)
        return_button.change_location((200, 450))
        starting_enviroment.update()
        starting_enviroment.draw(screen)
        cloud_1.animate(3)
        cloud_2.animate(-3)
        cloud_3.animate(4)
        cloud_4.animate(-2)
        if starting_screen == "started or setting":
            second_scene.draw(screen)
            mouse = pygame.mouse.get_pos()
            if start.is_clicked(mouse):
                image, rect = start.colors("Red", "Black")
            elif not start.is_clicked(mouse):
                image, rect = start.colors("Black","Red")
            screen.blit(image, rect)
            if setting_text.is_clicked(mouse):
                image, rect = setting_text.colors("Red", "Black")
            elif not setting_text.is_clicked(mouse):
                image, rect = setting_text.colors("Black","Red")
            screen.blit(image, rect)
        elif starting_screen == "setting":
            setting_screen.draw(screen)
            mouse = pygame.mouse.get_pos()
            
    elif scene == "scene1":
        for event in pygame.event.get():
            Library.close_game(event.type)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #Left click 
                if return_button.is_clicked(mouse):
                    scene = "starting"
                    continue
        return_button.change_location((30, 550))
        screen.blit(ingame_surface, (0,0))
        screen.blit(function_surface, (800,0))
        screen.blit(activate_surface, (0,500))
        
        scene1.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

