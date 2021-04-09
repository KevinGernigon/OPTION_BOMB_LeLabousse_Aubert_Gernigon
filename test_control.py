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
        self._motion = [0,0]    #Variable des sticks, motion [0] = axisX
        self._vitesse = 3

    def changeColor(self, color):   #Change la couleur du joueur, sert de test pour les boutons des manettes
        self.surf.fill((color))

    def movementKeyboard(self, pressed_keys, up, down, left, right):    #Déplace le joueur en fonction des touches clavier
        if pressed_keys[up]:
            self.rect.move_ip(0, -self._vitesse)

        elif pressed_keys[down]:
            self.rect.move_ip(0, self._vitesse)

        elif pressed_keys[left]:
            self.rect.move_ip(-self._vitesse, 0)

        elif pressed_keys[right]:
            self.rect.move_ip(self._vitesse, 0)

    def movementJoystick(self): #Bouge le perso en fonction du stick
            
        if abs(self._motion[0]) > abs(self._motion[1]): #Empêche le joueur de se déplacer en diagonale
            self._motion[1] = 0

        else:
            self._motion[0] = 0

        if self._motion[0] > 0.25:
            self.rect.move_ip(self._vitesse, 0)

        if self._motion[0] < -0.25:
            self.rect.move_ip(-self._vitesse, 0)

        if self._motion[1] > 0.25:
            self.rect.move_ip(0, self._vitesse)

        if self._motion[1] < -0.25:
            self.rect.move_ip(0, -self._vitesse) 

    def setMotion(self, axis, value):   #_motion récupère l'axe et la valeur du stick
        self._motion[axis] = value


#Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instantiate player. Right now, this is just a rectangle.
player1 = Player()  #Initialisation des joueurs
player2 = Player()

players = [player1, player2]    #Les joueurs sont placé dans une liste

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]



# Run until the user asks to quit
running = True

# Main loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event

        if event.type == JOYBUTTONDOWN: #Si le joueur appuie sur un boutton d'une manette
            print(event)

            if event.button == 0 and event.instance_id == 0:
                player1.changeColor((200,100,200))

            if event.button == 0 and event.instance_id == 1:
                player2.changeColor((200,100,100))


        if event.type == JOYAXISMOTION: #Si unstick d'une manette bouge
            print(event)
            if event.axis < 2 and event.instance_id < len(players): #on vérifie que c'est le stick gauche et que le numéro de la manette correspond a l'un des joueurs
                players[event.instance_id].setMotion(event.axis, event.value)   #Le joueur correspondant voit son attribut _motion prendre la valeur du stick


        if event.type == JOYDEVICEADDED:
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


    players[0].movementKeyboard(pressed_keys, K_UP, K_DOWN, K_LEFT, K_RIGHT)
    players[0].movementJoystick()

    players[1].movementKeyboard(pressed_keys, K_z, K_s, K_q, K_d)
    players[1].movementJoystick()


    # Fill the screen with white
    screen.fill((100, 100, 100))

    # Draw the player on the screen
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()