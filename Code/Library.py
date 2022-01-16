import pygame
from sys import exit

class ENVIROMENT(pygame.sprite.Sprite):
    """This class is the main class for sprite enviromental factor"""
    #Background
    def __init__(self, filename, scales, relative, pos_x, pos_y):
        """This funtion create a sprite with the provided image, scale, and position"""
        super().__init__()
        self.image_file = filename
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scales, self.image.get_height() *scales))
        if relative == "topleft":
            self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
        if relative == "center":
            self.rect = self.image.get_rect(center = (pos_x, pos_y))
    def animate(self, speed):
        """This function move the ENVIROMENT sprite looping through the scene using the provided speed"""
        self.rect.left += speed
        if self.rect.left > 1100:
            self.rect.right = - 100
        elif self.rect.right < -100:
            self.rect.left = 1100
    def is_clicked(self, pos):
        """This function check if the ENVIROMENT sprite collide at a point"""
        is_clicked = self.rect.collidepoint(pos)
        return is_clicked
    def transform_image(self, new_image, new_scale):
        """This function transform the image of the ENVIROMENT sprite without changing it position"""
        if new_image != None:
            self.image = pygame.image.load(new_image).convert_alpha()
        else:
            self.image = pygame.image.load(self.image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * new_scale, self.image.get_height() *new_scale))
        self.rect = self.image.get_rect(center = self.rect.center)
    def change_location(self, new_location):
        """This function change the location of the ENVIROMENT sprite"""
        self.rect = self.image.get_rect(topleft = new_location)
        
        
class PLAIN_TILE(pygame.sprite.Sprite):
    """This class is use for tile with 1 color"""
    def __init__(self, size, color, position):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)
    
class BUTTON(pygame.sprite.Sprite):
    def __init__(self, size, color, position):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)
        self.pos = position
        self.color = color
    def run_button(self, direction):
        self.command_dict = {"0": """player.go_up()\n""",
                            "90": """player.go_right()\n""",
            "180": """player.go_down()\n""",
            "270": """player.go_left()\n"""}
        return self.command_dict[direction]
    def change_direction(self, old_direction, turn):
        if turn == "left":
            new_direction = int(old_direction) + 90
        elif turn == "right":
            new_direction = int(old_direction) - 90
        if new_direction == 360:
            new_direction = 0
        elif new_direction == -90:
            new_direction = 270
        return str(new_direction)
    def change_location(self, newpos):
        self.rect.center = newpos



class PLAYER (pygame.sprite.Sprite):
    def __init__(self, img_link, starting_position):
        super().__init__()
        self.image = pygame.image.load(img_link).convert_alpha()
        self.image = pygame.transform.scale(self.image,(25, 25))
        self.rect = self.image.get_rect(center = starting_position)
    def go_up(self):
        self.rect.top -=50
    def go_down(self):
        self.rect.top +=50
    def go_left(self):
        self.rect.left -=50
    def go_right(self):
        self.rect.left +=50

class TEXT(pygame.sprite.Sprite):
    """This sprite class is use for text element"""
    def __init__(self, text, font, size, color, relative, pos_x, pos_y):
        """This function define the TEXT class
        Param: 
            text = string. The text printed.
            font = string. The filename to the font of the text.
            size = int or float. The size of the text
            color = list or string. The color of the text
            relative = "topleft" or "center". The relative position of the text
            pos_x = int. The x position of the text
            pos_y = int. The y position of the text"""
        super().__init__()
        self.font_type = pygame.font.Font(font, size)
        self.image = self.font_type.render(text, False, color)
        if relative == "topleft":
            self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
        if relative == "center":
            self.rect = self.image.get_rect(center = (pos_x, pos_y))
    def is_clicked(self, pos):
        is_clicked = self.rect.collidepoint(pos)
        return is_clicked
    def colors (self, new_color):
        masked = pygame.mask.from_surface(self.image)
        image_new =pygame.Surface((self.image.get_size()))
        image_new.fill(new_color)
        image_new = masked.to_surface(image_new, setcolor = new_color, unsetcolor= "White")
        image_new.set_colorkey("White")
        rect_new = self.rect.copy()
        return image_new, rect_new
    def change_text(self, new_text, new_color):
        self.image = self.font_type.render(new_text, False, new_color)
        self.rect = self.image.get_rect(center = self.rect.center)

class MAP_LAYOUT(pygame.sprite.Group):
    
    def __init__(self, mapfile, tile_size ,floor_im, gate_im):
        super().__init__()
        self.map = pygame.sprite.Group()
        self.void_tiles = pygame.sprite.Group()
        self.gate = pygame.sprite.Group()
        map_layout = open(mapfile, "r")
        map_layout = map_layout.read()
        map_layout = map_layout.split("\n")
        y = 0
        for row in map_layout:
            x = 0
            for col in row:
                
                if col == "0":
                    tile = PLAIN_TILE((25, 25), (225, 197, 190), (x*tile_size, y*tile_size))
                    self.void_tiles.add(tile)
                elif col == "2":
                    tile = ENVIROMENT(gate_im, 1, "topleft", x*tile_size, y*tile_size)
                    self.gate.add(tile)
                elif col == "1":
                    tile = ENVIROMENT(floor_im, 1, "topleft", x*tile_size, y*tile_size)
                elif col == "3": 
                    tile = ENVIROMENT(floor_im, 1, "topleft", x*tile_size, y*tile_size)
                    self.player_start = (x*tile_size, y*tile_size)
                elif col == "4":
                    tile = ENVIROMENT(floor_im, 1, "topleft", x*tile_size, y*tile_size)
                    self.key_pos  = (x*tile_size, y*tile_size)
                self.map.add(tile)
                x +=1
            y +=1
    def jump_to_the_void(self, sprite):
        collide = pygame.sprite.spritecollide(sprite, self.void_tiles, False)
        return (collide != [])
    def reach_the_gate(self, sprite):
        collide = pygame.sprite.spritecollide(sprite, self.gate, False)
        return (collide != [])
    


#Function
def close_game(event):
    if event == pygame.QUIT:
        pygame.quit()
        exit()

def duplicate(old_sprite):
    new_image = BUTTON(old_sprite.image.get_size(), old_sprite.color, old_sprite.pos)
    return new_image