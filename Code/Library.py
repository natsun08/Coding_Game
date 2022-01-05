import pygame
from sys import exit

from pygame.mask import Mask
class ENVIROMENT(pygame.sprite.Sprite):
    #Background
    def __init__(self, filename, scales, relative, pos_x, pos_y):
        super().__init__()
        self.image_file = filename
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scales, self.image.get_height() *scales))
        if relative == "topleft":
            self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
        if relative == "center":
            self.rect = self.image.get_rect(center = (pos_x, pos_y))
    def animate(self, speed):
        
        self.rect.left += speed
        if self.rect.left > 1100:
            self.rect.right = - 100
        elif self.rect.right < -100:
            self.rect.left = 1100
    def is_clicked(self, pos):
        is_clicked = self.rect.collidepoint(pos)
        return is_clicked
    def transform_image(self, new_image, new_scale):
        if new_image != None:
            self.image = pygame.image.load(new_image).convert_alpha()
        else:
            self.image = pygame.image.load(self.image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * new_scale, self.image.get_height() *new_scale))
        self.rect = self.image.get_rect(center = self.rect.center)
    def change_location(self, new_location):
        self.rect = self.image.get_rect(topleft = new_location)

class TEXT(pygame.sprite.Sprite):
    #Text
    def __init__(self, text, font, size, color, relative, pos_x, pos_y):
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
    def colors (self, new_color, old_color):
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
#Function
def close_game(event):
    if event == pygame.QUIT:
        pygame.quit()
        exit()