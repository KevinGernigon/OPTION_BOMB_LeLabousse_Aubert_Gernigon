import pygame
from pygame.locals import *
from datetime import datetime, timedelta

class Player(pygame.sprite.Sprite):
    def __init__(self, skin, position_x, position_y):
        super(Player, self).__init__()
        self.surf = pygame.image.load(skin).convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.case_x = 1
        self.case_y = 1
        self.x = 128 * self.case_x
        self.y = 128 * self.case_y

class Bomb:
    def __init__(self, bomb, perso1, perso2):
        # chargement des sprites
        self.bomb = pygame.image.load(bomb).convert()
        # place la bombe a une position non visible par default
        self.x = 1650
        self.y = 950
        self.case_x = 255
        self.case_y = 255
        self._time_created = datetime.now()
        # déclaration des variables de la classe
        self.perso1 = perso1
        self.perso2 = perso2
        self.explosion = 0

    def poser(self, x, y, bomb):
        #pose et arme la bombe
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / 128)
        self.case_y = int(y / 128)
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):
        #Explosion de la bombe

        # condition explosion de la bombe 3 seconde apres
        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            # change le sprite de la bombe en sprite d'explosion
            #self.bomb = pygame.image.load(image_explosion).convert()
            self.bomb.set_colorkey((0, 0, 0))
            self.explosion = 1

            try:

                # conditions de victoire (a simplifier)
                if self.case_x == self.perso1.case_x and self.case_y - 1 <= self.perso1.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso1.case_x <= self.case_x + 1 and self.case_y == self.perso1.case_y:
                    return 1

                if self.case_x == self.perso2.case_x and self.case_y - 1 <= self.perso2.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso2.case_x <= self.case_x + 1 and self.case_y == self.perso2.case_y:
                    return 1 

            except IndexError:
                # au cas ou la bombe est / detruit un bloc en dehors du terrain
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            # place la bombe a une position non visible apres l'explosion
            self.x = 1650
            self.y = 950
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0
