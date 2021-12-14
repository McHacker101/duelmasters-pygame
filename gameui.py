import pygame
from dm_backend import card_description


white = (255, 255, 255)
green = (5, 166, 61)
blue = (17, 175, 202)
black = (0, 0, 0)
violet = (238, 130, 238)
darkness = (89, 81, 140)
red = (166, 8, 21)
yellow = (247, 224, 99)

def civ_color(string):
    dict = {
        'Water': blue,
        'Fire': red,
        'Darkness': black,
        'Light': yellow,
        'Nature': green,
    }

    return dict.get(string, black)



class InfoUI():

    def __init__(self, screen, font):
        self.displayed_name = 'empty'
        # inputs
        # rect of inputs
        self.type_rect = pygame.rect.Rect(240, 170, 110, 20)
        self.power_rect = pygame.rect.Rect(240, 230, 110, 20)
        self.cost_rect = pygame.rect.Rect(240, 110, 110, 20)
        self.civil_rect = pygame.rect.Rect(240, 50, 70, 20)
        self.civil_color = pygame.rect.Rect(320, 50, 30, 20)
        self.nameRect = pygame.rect.Rect(23, 323, 323, 29)
        self.raceRect = pygame.rect.Rect(23, 363, 323, 29)
        self.imageRect = pygame.rect.Rect(25, 25, 200, 280)
        self.screen = screen
        self.font = font

    def write_text_wrapped(self, text, width, pos):
        """ Helps for wrapping text in a rect
            takes a text and the width to breakline the text
        """
        size = self.font.size(text)
        if size[0] > width:
            words = text.split()
            words_accumulated = []
            lines_to_render = []
            last_word = 0
            for word in words:
                if self.font.size(" ".join(words_accumulated))[0] > width:
                    popped = words_accumulated.pop()
                    lines_to_render.append(" ".join(words_accumulated))
                    words_accumulated = []
                    words_accumulated.append(popped)
                words_accumulated.append(word)
                last_word += 1
                if last_word == len(words):
                    lines_to_render.append(" ".join(words_accumulated))
            offset_Y = 0
            for lines in lines_to_render:
                rendered_line = self.font.render(lines, True, black)
                self.screen.blit(rendered_line, (pos[0], offset_Y + pos[1]))
                offset_Y += size[1]
                rendered_line = None
        else:
            self.font.render(text, True, black)



    def display_info_box(self):


        #all divisions of card info display
        self.label_power = pygame.draw.rect(self.screen, black, (240, 200, 110, 20), 2)
        self.label_type = pygame.draw.rect(self.screen, black, (240, 140, 110, 20), 2)
        self.label_cost = pygame.draw.rect(self.screen, black, (240, 80, 110, 20), 2)
        self.label_civil = pygame.draw.rect(self.screen, black, (240, 20, 110, 20), 2)
        self.race_border = pygame.draw.rect(self.screen, black, (20, 360, 330, 35), 2)
        self.name_border = pygame.draw.rect(self.screen, black, (20, 320, 330, 35), 2)
        self.card_border = pygame.draw.rect(self.screen, red, (20, 20, 210, 290), 2)
        self.details_border = pygame.draw.rect(self.screen, violet, (20, 400, 330, 300), 2)


        self.info = card_description.search(self.displayed_name)[0]
        # self.text = self.font.render(self.info['text'], True, black)
        self.image = pygame.image.load(self.info['image']).convert()
        self.image_size = self.image.get_size()
        self.display_card = pygame.transform.scale(self.image,(int(self.image_size[0] * 0.5), int(self.image_size[1] * 0.5)))
        self.civil = self.font.render(self.info['civilization'], True, black)
        self.type = self.font.render(self.info['type'], True, black)
        self.power = self.font.render(self.info['power'], True, black)
        self.cost = self.font.render(str(self.info['cost']), True, black)
        self.name = self.font.render(self.info['name'], True, black)
        self.race = self.font.render(self.info['race'], True, black)

        self.screen.blit(self.display_card, self.imageRect)
        self.write_text_wrapped(self.info['text'], self.details_border.width, (self.details_border.x, self.details_border.y))
        # self.screen.blit(self.text, self.details_border)
        self.screen.blit(self.civil, self.civil_rect)
        self.screen.blit(self.type, self.type_rect)
        self.screen.blit(self.power, self.power_rect)
        self.screen.blit(self.cost, self.cost_rect)
        self.screen.blit(self.power, self.power_rect)
        self.screen.blit(self.cost, self.cost_rect)
        self.screen.blit(self.name, self.nameRect)
        self.screen.blit(self.race, self.raceRect)
        pygame.draw.rect(self.screen, civ_color(self.info['civilization']), self.civil_color)

        self.screen.blit(self.font.render('Civilization:', True, black), self.label_civil)
        self.screen.blit(self.font.render('Mana Cost:', True, black), self.label_cost)
        self.screen.blit(self.font.render('Card Type', True, black), self.label_type)
        self.screen.blit(self.font.render('Power:', True, black), self.label_power)
        pygame.display.update()

        # display info on the infobox


    def display_card_info(self, card_name):
        if card_name != self.displayed_name:
            self.displayed_name = card_name




