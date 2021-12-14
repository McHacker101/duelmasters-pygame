import pygame
from pygame.locals import *
from dm_backend import card
import gameui

pygame.init()

display_x = 1280
display_y = 720

screen = pygame.display.set_mode([display_x, display_y])
running = True

display_asset_reload = False



white = (255, 255, 255)
green = (5, 166, 61)
blue = (17, 175, 202)
black = (0, 0, 0)
violet = (238, 130, 238)
darkness = (89, 81, 140)
red = (166, 8, 21)
yellow = (247, 224, 99)

font = pygame.font.Font('corbel.ttf', 15)


def civ_color(string):
    dict = {
        'Water': blue,
        'Fire': red,
        'Darkness': black,
        'Light': yellow,
        'Nature': green,
    }

    return dict.get(string, black)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('images/gui/newbg.jpg', [0, 0])
sample = card.Card('aqua hulcus', [640, 360])
sample2 = card.Card('chilias, the oracle', [840, 360])
infobox = gameui.InfoUI(screen, font)
all_card_in_field = []
field_me = [sample, sample2]
field_enemy = []
hand = []
graveyard = []
deck_me = []

def message(card_name, infoui):
    infoui.display_card_info(card_name)



def display_all_assets():
    screen.fill(white)
    screen.blit(BackGround.image, BackGround.rect)
    screen.blit(sample.hand_img, sample.rect)
    screen.blit(sample2.hand_img, sample2.rect)
    screen.fill(white, rect=[10, 10, 350, 700])

    for i in field_me:
        if i.rect.collidepoint(pygame.mouse.get_pos()):
            message(i.name, infobox)
    infobox.display_info_box()
    pygame.display.update()






while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        display_all_assets()



pygame.quit()
