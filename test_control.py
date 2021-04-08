# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# Move the sprite based on user keypresses
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        player.surf.fill(100, 100, 100)
    if pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        player.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        player.rect.move_ip(5, 0)

    # Keep player on the screen
    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > SCREEN_WIDTH:
        player.rect.right = SCREEN_WIDTH
    if player.rect.top <= 0:
        player.rect.top = 0
    if player.rect.bottom >= SCREEN_HEIGHT:
        player.rect.bottom = SCREEN_HEIGHT

#Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

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
        player.rect.move_ip(0,-5)

    if pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 5)

    if pressed_keys[K_LEFT]:
        player.rect.move_ip(-5, 0)
        
    if pressed_keys[K_RIGHT]:
        player.rect.move_ip(5, 0)

    # Fill the screen with white
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()