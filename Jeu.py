import pygame
from pygame.locals import *
from datetime import datetime, timedelta

from classes import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_SPACE,
    QUIT,
)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
image_bombe = "bomb.png"

# Move the sprite based on user keypresses

#Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Instantiate player. Right now, this is just a rectangle.
player = Player("perso.png", 200, 200)
player2 = Player("perso.png", 400, 400)

bombe = Bomb("bomb.png",player,player2)
bombe2 = Bomb("bomb.png",player2,player)


# Run until the user asks to quit
running = True

# Main loop
while running:
    
    pygame.time.Clock().tick(30)
    print(pygame.time.get_ticks())
    

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

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        player.rect.move_ip(0,-1)

    if pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 1)

    if pressed_keys[K_LEFT]:
        player.rect.move_ip(-1, 0)
        
    if pressed_keys[K_RIGHT]:
        player.rect.move_ip(8, 0)

    if pressed_keys[K_SPACE]:
        bombe.poser(player.x, player.y, image_bombe)


    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    screen.blit(player2.surf, player2.rect)
    screen.blit(bombe.bomb, (bombe.x, bombe.y))
    screen.blit(bombe2.bomb, (bombe2.x, bombe2.y))

    # Flip the display
    pygame.display.flip()

    game_over = bombe.exploser()
    if game_over == 1:
        running = False
        print("Game over")

# Done! Time to quit.
pygame.quit()