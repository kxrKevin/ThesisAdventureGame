import pygame
from sprite import Sprite
from input import is_key_pressed

class Player(Sprite):
    # Player constructor class
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def update(self):
        if is_key_pressed(pygame.K_UP):
            self.y -= 2
        if is_key_pressed(pygame.K_LEFT):
            self.x -= 2
        if is_key_pressed(pygame.K_DOWN):
            self.y += 2
        if is_key_pressed(pygame.K_RIGHT):
            self.x += 2 
    
    def inRed(self):
        if self.x < 285 and self.y < 250:
            return True
        return False

    def inBlue(self):
        if self.x > 285 and self.y < 250:
            return True
        return False

    def inGreen(self):
        if self.x < 285 and self.y > 250:
            return True
        return False

    def inYellow(self):
        if self.x > 285 and self.y > 250:
            return True
        return False