import pygame
import pytmx
import csv

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

class Player(pygame.sprite.Sprite):
    def __init__(self, skin, position_x, position_y):
        super(Player, self).__init__()
        self.surf = pygame.image.load(skin).convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y

# Move the sprite based on user keypresses

#Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Instantiate player. Right now, this is just a rectangle.
player = Player("perso.png", 200, 200)
bomb = pygame.image.load("bomb.png").convert_alpha()

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

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        player.rect.move_ip(0,-1)

    if pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 1)

    if pressed_keys[K_LEFT]:
        player.rect.move_ip(-1, 0)
        
    if pressed_keys[K_RIGHT]:
        player.rect.move_ip(1, 0)

    if pressed_keys[K_SPACE]:
        screen.blit(bomb, (player.rect.left, player.rect.top))
        pygame.display.flip()


    # Fill the screen with white
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()