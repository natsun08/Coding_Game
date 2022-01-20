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
scenes = ["starting","tutorial" ,"scene1", "scene2", "scene3", "ending/credit"]
scene = scenes[0]
starting_screen = "tittlescreen"
volumn = 1.0
is_sucess = False
get_drag = False
code_active = []
activate_code=False
is_tutorial = True
tile_size = 25
door_1 = "Game Asset\\Art\\door_1.png"
door_2 = "Game Asset\\Art\\door_2.png"
floor = "Game Asset\Art\\floor.png"


#SPRITE
#STARTING SCREEN ELEMENT
background_col = pygame.Surface((1000, 600))
background_col.fill((225, 197, 190))
sky_surface = Library.ENVIRONMENT("Game Asset\\Art\\Sky.png", 10, "topleft", 0, 0)
cloud_1 = Library.ENVIRONMENT("Game Asset\\Art\\Cloud1.png", 5, "topleft" , 80, 150)
cloud_2 = Library.ENVIRONMENT("Game Asset\\Art\\cloud2.png", 4, "topleft" ,600, 100)
cloud_3 = Library.ENVIRONMENT("Game Asset\\Art\\cloud2.png", 6, "topleft" ,300, 50)
cloud_4 = Library.ENVIRONMENT("Game Asset\\Art\\Cloud1.png", 7, "topleft" , 750, 150)
Logo = Library.ENVIRONMENT("Game Asset\\Art\\Gamename.png", 0.75,"center" , 500, 200)
scrolls = Library.ENVIRONMENT("Game Asset\\Art\\starting Scroll.png", 10, "center", 500, 300)
scroll_close_brown = Library.ENVIRONMENT("Game Asset\\Art\\scroll_close.png", 2.3, "center", 500, 400)
scroll_close_blue = Library.ENVIRONMENT("Game Asset\\Art\\scroll_close_2.png", 1, "center", 440, 350)
scroll_close_gold = Library.ENVIRONMENT("Game Asset\\Art\\scroll_close_3.png", 1, "center", 420, 430)
start = Library.TEXT("Start","Game Asset\\font\\NinjaPenguin.ttf", 70, "Black" , "center", 500, 350 )
setting_text = Library.TEXT("Setting","Game Asset\\font\\NinjaPenguin.ttf ", 70, "Black" , "center", 500, 430 )
#ENDING SCREEN ELEMENT
END_CERTIFICATE = Library.ENVIRONMENT("Game Asset\\Art\\certificate.png", 1, "topleft", 0, 0)
#SOUND
sound_icon = Library.ENVIRONMENT("Game Asset\\Art\\Sound_on.png", 1.5, "center", 400, 370)
sound_status = Library.TEXT("On","Game Asset\\font\\ninja-naruto.regular.ttf", 50, "Red", "topleft", 450, 350)
return_button = Library.ENVIRONMENT("Game Asset\\Art\\Return.png", 1, "topleft", 200, 450)
#IN-GAME SCREEN
function_surface = Library.ENVIRONMENT("Game Asset\Art\surf_doc.png",1,"topleft",800,0)
activate_surface = Library.ENVIRONMENT("Game Asset\Art\surf_ngang.png",1, "topleft", 0, 500)
victory_screen = Library.ENVIRONMENT("Game Asset\\Art\\starting Scroll.png", 10, "center", 500, 300)
next_stage_button = Library.ENVIRONMENT("Game Asset\\Art\\next.png", 1.5, "center" , 650, 450)
redo_button = Library.ENVIRONMENT("Game Asset\\Art\\redo.png", 1.5,"center" ,320, 450)
sucess = Library.TEXT("SUCCESED", "Game Asset\\font\\ninja-naruto.regular.ttf", 100, "Black", "center", 500, 300)
go_button = Library.BUTTON("Game Asset\Art\step.png", (100, 520))
turn_right_button = Library.BUTTON("Game Asset\\Art\\turn_clock.png", (250, 520))
turn_left_button = Library.BUTTON("Game Asset\\Art\\turn_counterclock.png", (180, 520))
compile_button = Library.ENVIRONMENT("Game Asset\Art\compile.png", 1, "topleft", 600, 520)
#MOUSE
mouse_sprite = Library.PLAIN_TILE((10, 10), "White", (0, 0))
new_copy = Library.PLAIN_TILE((20, 20), "White", (0, 0))

#GROUP
starting_enviroment = pygame.sprite.Group(sky_surface, cloud_1 , cloud_2,cloud_3, cloud_4 , Logo, scroll_close_brown)
second_scene = pygame.sprite.Group(scrolls, Logo, scroll_close_blue, start, setting_text, scroll_close_gold, return_button)
setting_screen = pygame.sprite.Group(scrolls, Logo, sound_status, sound_icon, return_button)
map_element_tutorial = Library.MAP_LAYOUT("Game Asset\\Map\\First_tutorial_map.txt", tile_size,floor, door_1 ,door_2 )
map_element_1 = Library.MAP_LAYOUT("Game Asset\\Map\\First_map_layout.txt", tile_size, floor, door_1 ,door_2 )
map_element_2 = Library.MAP_LAYOUT("Game Asset\\Map\\Second_map_layout.txt", tile_size,floor, door_1 ,door_2)
map_element_3 = Library.MAP_LAYOUT("Game Asset\\Map\\Third_map_layout.txt", tile_size, floor, door_1 ,door_2 )
tutorial = Library.ENVIRONMENT("Game Asset\\Art\\tutorial.png", 1, "center", 500, 300)
player = Library.PLAYER("Game Asset\\Art\\Player.png", (0, 0))
key = Library.ENVIRONMENT("Game Asset\\Art\\key.png", 1, "center", -100, -100)

players = pygame.sprite.GroupSingle(player)
buttons = pygame.sprite.Group()
run_buttons = pygame.sprite.Group()
turn_counter_clockwise_buttons = pygame.sprite.Group()
turn_clockwise_buttons = pygame.sprite.Group()
tutorial_screen = pygame.sprite.Group(tutorial)
keys = pygame.sprite.Group(key)
scroll_2 = pygame.sprite.Group(activate_surface, go_button, return_button, turn_right_button,turn_left_button, compile_button )
scroll_3 = pygame.sprite.Group(function_surface)
WIN_SCREEN = pygame.sprite.Group(victory_screen, sucess, redo_button, next_stage_button)
Ending = pygame.sprite.Group(END_CERTIFICATE)
map_element_dict = {"tutorial": map_element_tutorial,
                    "scene1" : map_element_1,
                    "scene2" : map_element_2,
                    "scene3" : map_element_3}

#function
def map_draw(map_element):
    """This function draw the element on the screen depend on the map element"""
    screen.blit(background_col, (0,0))
    return_button.change_location((30, 550))
    map_element.map.draw(screen)
    scroll_3.draw(screen)
    scroll_2.draw(screen)
    keys.draw(screen)
    buttons.draw(screen)
    players.draw(screen)

#STARTING SCREEN
while True:
    if activate_code and code_active != []:
        #Run the script
        for event in pygame.event.get():
            Library.close_game(event.type)
        exec(code_active[x])
        map_draw(map_element_dict[scene])
        pygame.display.update()
        pygame.event.pump()
        clock.tick(5)
        x+=1
        if have_key:
            #If the game have key then player must reach the key in order to finish the game
            if player.rect.collidepoint(map_element.key_pos):
                key_to_gate = True
                key.rect.center = (-100, -100)
        if (map_element.reach_the_gate(player))  and (key_to_gate or not have_key):
            is_sucess = True
        if map_element.jump_to_the_void(player):
            #If the player touch the non floor tile they will be teleport to the start and end the run
            player.rect.center = map_element.player_start
            x = 0
            run = "done"
        if x == len(code_active) or is_sucess:
            #When the run through all the code or reach the gate
            run = "done"
        if run == "done":
            #Reset the player to the start and clear the script when the run is done
            activate_code = False
            key_to_gate = False
            code_active = []
            player.rect.center = map_element.player_start
        continue
    if is_sucess:
        #Success screen
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            Library.close_game(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if redo_button.rect.collidepoint(mouse):
                    #Go back to the stage if pressed redo
                    is_sucess = False
                if next_stage_button.rect.collidepoint(mouse):
                    #Go to the next stage
                    scene_pos = scenes.index(scene)
                    scene = scenes[scene_pos + 1]
                    buttons.empty()
                    is_sucess = False
        WIN_SCREEN.draw(screen)
        pygame.display.update()
        clock.tick(5)
        continue
    else:
        if scene == "starting":#Home screen 
            for event in pygame.event.get():
                Library.close_game(event.type)
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #When Left click 
                    if scroll_close_brown.is_clicked(mouse) and starting_screen == "tittlescreen": #Check if the user click the brown scroll at start
                        starting_screen = "started or setting"
                        break
                    elif starting_screen == "started or setting": #If we switch to starting screen
                        if start.is_clicked(mouse): #If player choose start
                            scene = scenes[1]
                            continue
                        elif setting_text.is_clicked(mouse):#If player choose setting
                            starting_screen = "setting"
                            break
                        elif return_button.is_clicked(mouse): #If player choose return
                            starting_screen = "tittlescreen"
                    if starting_screen == "setting": #switch to setting screen
                        if sound_status.is_clicked(mouse) or sound_icon.is_clicked(mouse): #Change volumn
                            if volumn > 0.0:
                                sound_status.change_text("Off", "Black")#Change text to Off 
                                volumn = 0.0 #Turn off music
                                sound_icon.transform_image("Game Asset\\Art\\Sound_off.png", 1.5)
                            elif volumn == 0.0:
                                volumn = 1.0 #Turn on music
                                sound_status.change_text("On", "Red")#Change text to On 
                                sound_icon.transform_image("Game Asset\\Art\\Sound_on.png", 1.5)
                            pygame.mixer.music.set_volume(volumn)
                            setting_screen.update() #Update the group
                        elif return_button.is_clicked(mouse): 
                            starting_screen =  "started or setting"
            if scroll_close_brown.is_clicked(mouse): 
                scroll_close_brown.transform_image(new_image=None, new_scale=3)#Zoom the icon when hover
            elif not scroll_close_brown.is_clicked(mouse):
                scroll_close_brown.transform_image(new_image=None, new_scale=2.3)#Minimize the icon when not hover
            return_button.change_location((200, 450))
            starting_enviroment.update()
            starting_enviroment.draw(screen)
            #The cloud float in diffirent speed
            cloud_1.animate(3)
            cloud_2.animate(-3)
            cloud_3.animate(4)
            cloud_4.animate(-2)
            if starting_screen == "started or setting":
                second_scene.draw(screen)
                mouse = pygame.mouse.get_pos()
                #Change the color of the text based on if the mouse is hovering on the text. 
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
            #For general game map
            map_element = map_element_dict[scene]
            player.rect.center = map_element.player_start
            try:
                #See if the map require a key or not
                key.rect.center = map_element.key_pos
                have_key = True
            except AttributeError:
                have_key = False
            for event in pygame.event.get():
                Library.close_game(event.type)
                mouse = pygame.mouse.get_pos()
                mouse_sprite.rect.center = mouse
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #when Left click 
                    if is_tutorial:
                        #Turn off the tutorial in the first round
                        is_tutorial = False
                    if return_button.is_clicked(mouse):
                        scene = "starting"
                        continue
                    if not get_drag and pygame.sprite.spritecollide(mouse_sprite, buttons, False) != []:
                        #Delete a button when clicked
                        pygame.sprite.spritecollide(mouse_sprite, buttons, True)
                    if go_button.rect.collidepoint(mouse):
                        #start draging a button
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
                        #Put all the code into code_active 
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
                        key_to_gate = False
                if get_drag:
                    #Drag the buttons
                    new_copy.change_location(mouse)
                    buttons.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    #Drop off the buttons
                    if not new_copy.rect.colliderect(function_surface.rect):
                        #Remove the buttons if the drop off spot isn't the function surface
                        new_copy.kill()
                        buttons.update()
                    get_drag = False
            map_draw(map_element)
            if is_tutorial:
                #Draw the tutorial if this is the first time the game open
                tutorial_screen.draw(screen)
            
        elif scene == "ending/credit":
            for event in pygame.event.get():
                Library.close_game(event.type)
            Ending.draw(screen)
        pygame.display.update()
        clock.tick(60)
