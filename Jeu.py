import pygame

from pygame.locals import *
from datetime import datetime, timedelta

from classes import *

from pygame.locals import (
    K_z,
    K_q,
    K_s,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    JOYBUTTONDOWN,
    JOYAXISMOTION,
    JOYHATMOTION,
    JOYDEVICEADDED,
    JOYDEVICEREMOVED,
    QUIT,
)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

image_bombe = "bomb.png"

walls_data = [[10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 11], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, 8, 2, -1, -1, -1, 2, -1, -1, -1, 2, 9, -1, 5], [4, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 5], [4, -1, -1, -1, -1, -1, 2, 2, 2, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, 2, 2, 2, -1, -1, -1, -1, -1, 2, 2, 2, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, 2, 2, 2, -1, -1, -1, -1, -1, 5], [4, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 5], [4, -1, 6, 3, -1, -1, -1, 3, -1, -1, -1, 3, 7, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13]]
walls_img_list = []

rows = 15
wall_types = 14
tile_size = 48
cols = 15
wall_drawn = False

for x in range (2, wall_types):
    img = pygame.image.load(f'assets/{x}.png')
    img = pygame.transform.scale(img, (tile_size, tile_size))
    walls_img_list.append(img)

top_wall = pygame.Rect(0,0, 720, 33)
bottom_wall = pygame.Rect(0, 672, 720, 48)
left_wall = pygame.Rect(0, 0, 48, 720)
right_wall = pygame.Rect(672, 0, 48, 720)

# Move the sprite based on user keypresses

#Initialize pygame
pygame.init()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Instantiate player. Right now, this is just a rectangle.
background = pygame.image.load("assets/background.png").convert_alpha()

def draw_walls():
    for y, row in enumerate(walls_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                #print(tile)
                screen.blit(walls_img_list[tile-2], (x * tile_size, y * tile_size))
        
player = Player("assets/joueur_bleu.png", 48, 48)
player2 = Player("assets/joueur_vert.png", 624, 624)
players = [player, player2]

bombe = Bomb("bomb.png",player,player2)
bombe2 = Bomb("bomb.png",player2,player)

# Run until the user asks to quit
running = True

# Main loop
while running:
    
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    
    if event.type == JOYAXISMOTION: #Si unstick d'une manette bouge
            print(event)
            if event.axis < 2 and event.instance_id < len(players): #on vérifie que c'est le stick gauche et que le numéro de la manette correspond a l'un des joueurs
                players[event.instance_id].setMotion(event.axis, event.value)   #Le joueur correspondant voit son attribut _motion prendre la valeur du stick


    if event.type == JOYDEVICEADDED:
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    if event.type == JOYDEVICEREMOVED:
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_SPACE]:
        bombe.poser(player.x, player.y, image_bombe)

    if event.type == JOYBUTTONDOWN:
        bombe.poser(player2.x, player2.y, image_bombe)

    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    draw_walls()
    screen.blit(player.surf, player.rect)
    screen.blit(player2.surf, player2.rect)
    screen.blit(bombe.bomb, (bombe.x, bombe.y))
    screen.blit(bombe2.bomb, (bombe2.x, bombe2.y))

    # Flip the display
    pygame.display.flip()
    players[0].movementKeyboard(pressed_keys, K_UP, K_DOWN, K_LEFT, K_RIGHT)
    players[0].movementJoystick()

    players[1].movementKeyboard(pressed_keys, K_z, K_s, K_q, K_d)
    players[1].movementJoystick()

    game_over = bombe.exploser()
    if game_over == 1:
        running = False
        print("Game over")

# Done! Time to quit.
pygame.quit()