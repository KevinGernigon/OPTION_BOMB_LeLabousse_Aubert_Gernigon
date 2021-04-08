# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updatd to conform to flake8 and black standards
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

    def changeColor(self, color):
        self.surf.fill((color))


    def movementKeyboard(self, pressed_keys, up, down, left, right):
        if pressed_keys[up]:
            self.rect.move_ip(0, -5)
        if pressed_keys[down]:
            self.rect.move_ip(0, 5)
        if pressed_keys[left]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[right]:
            self.rect.move_ip(5, 0)

    def movementJoystick(self, motion):
        self.rect.move_ip(motion[0]*10, motion[1]*10)

def slotDisponible(liste):
    for i in liste:
        if liste[i] == 0:
            return i
        else:
            return len(liste)



#Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instantiate player. Right now, this is just a rectangle.
player1 = Player()
player2 = Player()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

motion1 = [0, 0]
motion2 = [0, 0]
manette = []

# Run until the user asks to quit
running = True

# Main loop
while running:

    if abs(motion1[0]) < 0.1:
        motion1[0] = 0

    if abs(motion1[1]) < 0.1:
        motion1[1] = 0

    if abs(motion2[0]) < 0.1:
        motion2[0] = 0

    if abs(motion2[1]) < 0.1:
        motion2[1] = 0
    

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event

        if event.type == JOYBUTTONDOWN:
            print(event)

            if event.button == 0 and event.joy == 0:
                player1.changeColor((100,100,100))
            if event.button == 0 and event.joy == 1:
                player2.changeColor((200,100,100))


        if event.type == JOYAXISMOTION:
            print(event)
            if event.axis < 2 and event.joy == 0:
                motion1[event.axis] = event.value

            if event.axis < 2 and event.joy == 1:
                motion2[event.axis] = event.value 

        if event.type == JOYDEVICEADDED:
            print(event)
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()


    player1.movementKeyboard(pressed_keys, K_UP, K_DOWN, K_LEFT, K_RIGHT)
    player1.movementJoystick(motion1)

    player2.movementKeyboard(pressed_keys, K_z, K_s, K_q, K_d)
    player2.movementJoystick(motion2)

    # Fill the screen with white
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()