import pygame
from sys import exit
import Code.Library as Library
#MANDATORY
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Platform')
clock = pygame.time.Clock()

#MUSIC (Will be change to free music later)
pygame.mixer.music.load("Game Asset\\Music\\Omoide Tsuzuri - Akatsuki.wav")
#song link: https://www.youtube.com/watch?v=yzQyzvsv2NY
pygame.mixer.music.play(-1)

#VARIABLE
scenes = ["starting", "scene1", "scene2", "scene3", "ending/credit"]
scene = scenes[0]
#Vị trí cho scene
starting_screen = "tittlescreen"
volumn = 1.0
is_sucess = False
get_drag = False
code_active = []
activate_code=False


#Surface
function_surface = Library.PLAIN_TILE((200, 600), "Gray",  (800,0))
activate_surface = Library.PLAIN_TILE((800, 100), "White", (0, 500))

#Sprite
sky_surface = Library.ENVIROMENT("Game Asset\\Art\\Sky.png", 10, "topleft", 0, 0)
cloud_1 = Library.ENVIROMENT("Game Asset\\Art\\Cloud1.png", 5, "topleft" , 80, 150)
cloud_2 = Library.ENVIROMENT("Game Asset\\Art\\cloud2.png", 4, "topleft" ,600, 100)
cloud_3 = Library.ENVIROMENT("Game Asset\\Art\\cloud2.png", 6, "topleft" ,300, 50)
cloud_4 = Library.ENVIROMENT("Game Asset\\Art\\Cloud1.png", 7, "topleft" , 750, 150)
Logo = Library.ENVIROMENT("Game Asset\\Art\\Gamename.png", 0.75,"center" , 500, 200)
scrolls = Library.ENVIROMENT("Game Asset\\Art\\starting Scroll.png", 10, "center", 500, 300)
scroll_close_brown = Library.ENVIROMENT("Game Asset\\Art\\scroll_close.png", 2.3, "center", 500, 400)
scroll_close_blue = Library.ENVIROMENT("Game Asset\\Art\\scroll_close_2.png", 1, "center", 440, 350)
scroll_close_gold = Library.ENVIROMENT("Game Asset\\Art\\scroll_close_3.png", 1, "center", 420, 430)
start = Library.TEXT("Start","Game Asset\\font\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 350 )
setting_text = Library.TEXT("Setting","Game Asset\\font\\NinjaPenguin.ttf ", 70, "Black" , "center", 500, 430 )
sound_icon = Library.ENVIROMENT("Game Asset\\Art\\Sound_on.png", 1.5, "center", 400, 370)
sound_status = Library.TEXT("On","Game Asset\\font\\ninja-naruto.regular.ttf", 50, "Red", "topleft", 450, 350)
return_button = Library.ENVIROMENT("Game Asset\\Art\\Return.png", 1, "topleft", 200, 450)
victory_screen = Library.PLAIN_TILE((800, 500), "pink", (100, 50))
next_stage_button = Library.PLAIN_TILE((100, 50), "Blue", (650, 450))
redo_button = Library.PLAIN_TILE((100, 50), "red", (300, 450))
sucess = Library.TEXT("SUCCESED", "Game Asset\\font\\ninja-naruto.regular.ttf", 100, "Black", "center", 500, 300)
go_button = Library.BUTTON((40, 40),"Blue", (100, 510))
turn_right_button = Library.BUTTON((40, 40),"Red", (230, 510))
turn_left_button = Library.BUTTON((40, 40),"Green", (180, 510))
compile_button = Library.ENVIROMENT("Game Asset\\Art\\Sound_on.png", 1.5, "center", 810, 370)
mouse_sprite = Library.PLAIN_TILE((10, 10), "White", (0, 0))
new_copy = Library.PLAIN_TILE((20, 20), "White", (0, 0))

#GROUP
starting_enviroment = pygame.sprite.Group(sky_surface, cloud_1 , cloud_2,cloud_3, cloud_4 , Logo, scroll_close_brown)
second_scene = pygame.sprite.Group(scrolls, Logo, scroll_close_blue, start, setting_text, scroll_close_gold, return_button)
setting_screen = pygame.sprite.Group(scrolls, Logo, sound_status, sound_icon, return_button)
map_element_1 = Library.MAP_LAYOUT("Game Asset\\Map\\First_map_layout.txt", 25, "Game Asset\\Art\\test.png","Game Asset\\Art\\test.png" )
map_element_2 = Library.MAP_LAYOUT("Game Asset\\Map\\First_map_layout.txt", 25, "Game Asset\\Art\\test.png","Game Asset\\Art\\test.png" )
#Thay tên file txt để đổi map 2
map_element_3 = Library.MAP_LAYOUT("Game Asset\\Map\\First_map_layout.txt", 25, "Game Asset\\Art\\test.png","Game Asset\\Art\\test.png" )
#Thay tên file txt để đổi map 3
player = Library.PLAYER("Game Asset\\Art\\scroll_close_3.png", (0, 0))
players = pygame.sprite.GroupSingle(player)
buttons = pygame.sprite.Group()
run_buttons = pygame.sprite.Group()
turn_counter_clockwise_buttons = pygame.sprite.Group()
turn_clockwise_buttons = pygame.sprite.Group()
scroll_2 = pygame.sprite.Group(activate_surface, go_button, return_button, turn_right_button,turn_left_button )
scroll_3 = pygame.sprite.Group(function_surface, compile_button)
WIN_SCREEN = pygame.sprite.Group(victory_screen, sucess, redo_button, next_stage_button)
map_element_dict = {"scene1" : map_element_1,
                    "scene2" : map_element_2,
                    "scene3" : map_element_3}

#function
def map_draw(map_element):
    return_button.change_location((30, 550))
    map_element.map.draw(screen)
    scroll_3.draw(screen)
    scroll_2.draw(screen)
    buttons.draw(screen)
    players.draw(screen)

#STARTING SCREEN
while True:
    if activate_code and code_active != []:
        for event in pygame.event.get():
            Library.close_game(event.type)
        exec(code_active[x])
        map_draw(map_element_dict[scene])
        pygame.display.update()
        pygame.event.pump()
        clock.tick(5)
        x+=1
        if map_element.reach_the_gate(player): #or code_active != []: #<- code này để test màn hình success
            is_sucess = True
        if map_element.jump_to_the_void(player):
            player.rect.center = map_element.player_start
            x = 0
            run = "done"
        if x == len(code_active) or is_sucess:
            run = "done"
        if run == "done":
            activate_code = False
            code_active = []
            player.rect.center = map_element.player_start
        continue
    if is_sucess:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            Library.close_game(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if redo_button.rect.collidepoint(mouse):
                    scene = scenes[0]
                    is_sucess = False
                if next_stage_button.rect.collidepoint(mouse):
                    scene_pos = scenes.index(scene)
                    scene = scenes[scene_pos + 1]
                    buttons.empty()
                    is_sucess = False
        WIN_SCREEN.draw(screen)
        pygame.display.update()
        clock.tick(5)
        continue
    else:
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
                                sound_icon.transform_image("Game Asset\\Art\\Sound_off.png", 1.5)
                            elif volumn == 0.0:
                                volumn = 1.0
                                sound_status.change_text("On", "Red")
                                sound_icon.transform_image("Game Asset\\Art\\Sound_on.png", 1.5)
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
                    image, rect = start.colors("Red")
                elif not start.is_clicked(mouse):
                    image, rect = start.colors("Black")
                screen.blit(image, rect)
                if setting_text.is_clicked(mouse):
                    image, rect = setting_text.colors("Red")
                elif not setting_text.is_clicked(mouse):
                    image, rect = setting_text.colors("Black")
                screen.blit(image, rect)
            elif starting_screen == "setting":
                setting_screen.draw(screen)
                mouse = pygame.mouse.get_pos()
                
        elif scene in scenes[1:-1]:
            map_element = map_element_dict[scene]
            player.rect.center = map_element.player_start
            for event in pygame.event.get():
                Library.close_game(event.type)
                mouse = pygame.mouse.get_pos()
                mouse_sprite.rect.center = mouse
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Left click 
                    if return_button.is_clicked(mouse):
                        scene = "starting"
                        continue
                    if not get_drag and pygame.sprite.spritecollide(mouse_sprite, buttons, False) != []:
                        pygame.sprite.spritecollide(mouse_sprite, buttons, True)
                    if go_button.rect.collidepoint(mouse):
                        get_drag = True
                        new_copy = Library.duplicate(go_button)
                        run_buttons.add(new_copy)
                        buttons.add(new_copy)
                    elif turn_right_button.rect.collidepoint(mouse):
                        get_drag = True
                        new_copy = Library.duplicate(turn_right_button)
                        turn_counter_clockwise_buttons.add(new_copy)
                        buttons.add(new_copy)
                    elif turn_left_button.rect.collidepoint(mouse):
                        get_drag = True
                        new_copy = Library.duplicate(turn_left_button)
                        turn_clockwise_buttons.add(new_copy)
                        buttons.add(new_copy)
                    
                    if buttons.sprites() != [] and compile_button.rect.collidepoint(mouse):
                        all_buttons = buttons.sprites()
                        direction = "0"
                        for sprite in all_buttons:
                            if sprite in run_buttons:
                                code_active.append(new_copy.run_button(direction))
                            elif sprite in turn_counter_clockwise_buttons:
                                direction = new_copy.change_direction(direction, "left")
                            elif sprite in turn_clockwise_buttons:
                                direction = new_copy.change_direction(direction, "right")
                        x = 0
                        run = "start"
                        activate_code = True
                if get_drag:
                    new_copy.change_location(mouse)
                    buttons.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    if not new_copy.rect.colliderect(function_surface.rect):
                        new_copy.kill()
                        buttons.update()
                    get_drag = False
            map_draw(map_element)
            
        elif scene == "ending/credit":
            for event in pygame.event.get():
                Library.close_game(event.type)
            starting_enviroment.draw(screen)
        pygame.display.update()
        clock.tick(60)

