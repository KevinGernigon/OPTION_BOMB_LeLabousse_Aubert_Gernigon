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
        self.x = 128*self.case_x
        self.y = 128*self.case_y
        self._motion = [0,0]

    def movementKeyboard(self, pressed_keys, up, down, left, right):    #Déplace le joueur en fonction des touches clavier
        if (self.rect.x >= 48 and self.rect.x <= 624 and self.rect.y > 48) and not (self.rect.x >= 144 and self.rect.x < 192 and self.rect.y == 144) and not (self.rect.x > 48 and self.rect.x < 144 and self.rect.y == 192) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 144) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 144) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y == 192) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 240) and not (self.rect.x > 48 and self.rect.x < 240 and self.rect.y == 384) and not (self.rect.x > 432 and self.rect.x < 624 and self.rect.y == 384) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 528) and not (self.rect.x > 48 and self.rect.x < 192 and self.rect.y == 624) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 624) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 624):  
            if pressed_keys[up]:
                self.rect.move_ip(0,-1)

        if (self.rect.x >= 48 and self.rect.x <= 624 and self.rect.y < 624) and not (self.rect.x > 48 and self.rect.x < 192 and self.rect.y == 48) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 48) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 48) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 144) and not (self.rect.x > 48 and self.rect.x < 240 and self.rect.y == 288) and not (self.rect.x > 432 and self.rect.x < 624 and self.rect.y == 288) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 432) and not (self.rect.x > 48 and self.rect.x < 144 and self.rect.y == 480) and not (self.rect.x > 96 and self.rect.x < 192 and self.rect.y == 528) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 528) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 528) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y == 480):
            if pressed_keys[down]:
                self.rect.move_ip(0, 1)

        if (self.rect.x > 48 and self.rect.y >= 48 and self.rect.y <= 624) and not (self.rect.x == 192 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x == 144 and self.rect.y > 96 and self.rect.y < 192) and not (self.rect.x == 384 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x == 624 and self.rect.y > 48 and self.rect.y < 192) and not (self.rect.x == 432 and self.rect.y > 144 and self.rect.y < 240) and not (self.rect.x == 240 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 624 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 432 and self.rect.y > 432 and self.rect.y < 528) and not (self.rect.x == 144 and self.rect.y > 480 and self.rect.y < 624) and not (self.rect.x == 192 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 384 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 624 and self.rect.y > 480 and self.rect.y < 624):
            if pressed_keys[left]:
                self.rect.move_ip(-1, 0)

        if (self.rect.x < 624 and self.rect.y >= 48 and self.rect.y <= 624) and not (self.rect.y > 48 and self.rect.y < 192 and self.rect.x == 48) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y > 96 and self.rect.y < 192) and not (self.rect.x > 240 and self.rect.x < 288 and self.rect.y > 144 and self.rect.y < 240) and not (self.rect.x == 48 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 432 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 240 and self.rect.y > 432 and self.rect.y < 528) and not (self.rect.x == 48 and self.rect.y > 480 and self.rect.y < 624) and not (self.rect.x == 288 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 480 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 528 and self.rect.y > 480 and self.rect.y < 624):
            if pressed_keys[right]:
                self.rect.move_ip(1, 0)

    def movementJoystick(self): #Bouge le perso en fonction du stick
            
        #if abs(self._motion[0]) > abs(self._motion[1]): #Empêche le joueur de se déplacer en diagonale
        #    self._motion[1] = 0

        #else:
        #    self._motion[0] = 0
    
        if (self.rect.x >= 48 and self.rect.x <= 624 and self.rect.y > 48) and not (self.rect.x >= 144 and self.rect.x < 192 and self.rect.y == 144) and not (self.rect.x > 48 and self.rect.x < 144 and self.rect.y == 192) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 144) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 144) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y == 192) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 240) and not (self.rect.x > 48 and self.rect.x < 240 and self.rect.y == 384) and not (self.rect.x > 432 and self.rect.x < 624 and self.rect.y == 384) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 528) and not (self.rect.x > 48 and self.rect.x < 192 and self.rect.y == 624) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 624) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 624):  
            if self._motion[1] < -0.25:
                self.rect.move_ip(0,-1)

        if (self.rect.x >= 48 and self.rect.x <= 624 and self.rect.y < 624) and not (self.rect.x > 48 and self.rect.x < 192 and self.rect.y == 48) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 48) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 48) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 144) and not (self.rect.x > 48 and self.rect.x < 240 and self.rect.y == 288) and not (self.rect.x > 432 and self.rect.x < 624 and self.rect.y == 288) and not (self.rect.x > 240 and self.rect.x < 432 and self.rect.y == 432) and not (self.rect.x > 48 and self.rect.x < 144 and self.rect.y == 480) and not (self.rect.x > 96 and self.rect.x < 192 and self.rect.y == 528) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y == 528) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y == 528) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y == 480):
            if self._motion[1] > 0.25:
                self.rect.move_ip(0, 1)

        if (self.rect.x > 48 and self.rect.y >= 48 and self.rect.y <= 624) and not (self.rect.x == 192 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x == 144 and self.rect.y > 96 and self.rect.y < 192) and not (self.rect.x == 384 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x == 624 and self.rect.y > 48 and self.rect.y < 192) and not (self.rect.x == 432 and self.rect.y > 144 and self.rect.y < 240) and not (self.rect.x == 240 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 624 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 432 and self.rect.y > 432 and self.rect.y < 528) and not (self.rect.x == 144 and self.rect.y > 480 and self.rect.y < 624) and not (self.rect.x == 192 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 384 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 624 and self.rect.y > 480 and self.rect.y < 624):
            if self._motion[0] < -0.25:
                self.rect.move_ip(-1, 0)

        if (self.rect.x < 624 and self.rect.y >= 48 and self.rect.y <= 624) and not (self.rect.y > 48 and self.rect.y < 192 and self.rect.x == 48) and not (self.rect.x > 288 and self.rect.x < 384 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x > 480 and self.rect.x < 624 and self.rect.y > 48 and self.rect.y < 144) and not (self.rect.x > 528 and self.rect.x < 624 and self.rect.y > 96 and self.rect.y < 192) and not (self.rect.x > 240 and self.rect.x < 288 and self.rect.y > 144 and self.rect.y < 240) and not (self.rect.x == 48 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 432 and self.rect.y > 288 and self.rect.y < 384) and not (self.rect.x == 240 and self.rect.y > 432 and self.rect.y < 528) and not (self.rect.x == 48 and self.rect.y > 480 and self.rect.y < 624) and not (self.rect.x == 288 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 480 and self.rect.y > 528 and self.rect.y < 624) and not (self.rect.x == 528 and self.rect.y > 480 and self.rect.y < 624):
            if self._motion[0] > 0.25:
                self.rect.move_ip(1, 0)

    def setMotion(self, axis, value):   #_motion récupère l'axe et la valeur du stick
        self._motion[axis] = value


class Bomb:
    def __init__(self, bomb, perso1, perso2):
        # chargement des sprites
        self.bomb = pygame.image.load(bomb).convert_alpha()
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
        self.bomb = pygame.image.load(bomb).convert_alpha()
        #self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = x
        self.case_y = y
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):
        #Explosion de la bombe

        # condition explosion de la bombe 3 seconde apres
        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            # change le sprite de la bombe en sprite d'explosion
            image_explosion = "explodstart.png"
            self.bomb = pygame.image.load(image_explosion).convert_alpha()
            self.bomb.set_colorkey((0, 0, 0))
            self.explosion = 1

            try:

                # conditions de victoire (a simplifier)
                if self.case_x - 150 <= self.perso1.rect.x <= self.case_x + 150 and self.case_y - 150 <= self.perso1.rect.y <= self.case_y + 150:
                    return 1

                if self.case_x - 150 <= self.perso2.rect.x <= self.case_x + 150 and self.case_y - 150 <= self.perso2.rect.y <= self.case_y + 150:
                    return 1

            except IndexError:
                # au cas ou la bombe est / detruit un bloc en dehors du terrain
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            # place la bombe a une position non visible apres l'explosion
            self.x = 16500
            self.y = 9500
            self.case_x = 2550
            self.case_y = 2550
            self.explosion = 0