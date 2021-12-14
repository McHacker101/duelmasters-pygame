from random import randrange
import pygame
from dm_backend import card_description

class Card(pygame.sprite.Sprite):
    def __init__(self, name, location):
        self.mouse_hover = False
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.name = name
        self.info = card_description.search(name)
        self.image = pygame.image.load(self.info[0]["image"]).convert()
        self.size = self.image.get_size()
        self.hand_img = pygame.transform.scale(self.image, (int(self.size[0]*0.2), int(self.size[1]*0.2)))
        self.rect = self.hand_img.get_rect()
        self.rect.left, self.rect.top = location
        # if self.rect.collidepoint(pygame.mouse.get_pos()):
        #     message(self.name, infobox)
    
    def get_info_and_status(self):
        return self.info[0], self.mouse_hover

    def get_rect(self):
        return self.rect



