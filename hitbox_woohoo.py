import pygame

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

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

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

class Player(pygame.sprite.Sprite):
    def __init__(self, skin, position_x, position_y):
        super(Player, self).__init__()
        self.surf = pygame.image.load(skin).convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = pygame.Rect(0, 64, 45, 64)
        self.rect.x = position_x
        self.rect.y = position_y

# Move the sprite based on user keypresses

#Initialize pygame
pygame.init()

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
bomb = pygame.image.load("assets/bomb.png").convert_alpha()

# Run until the user asks to quit
running = True

# Main loop
while running:
    
    print(player.rect.x)
    print(player.rect.y)
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
    if (player.rect.x >= 48 and player.rect.x <= 624 and player.rect.y > 48) and not (player.rect.x >= 144 and player.rect.x < 192 and player.rect.y == 144) and not (player.rect.x > 48 and player.rect.x < 144 and player.rect.y == 192) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 144) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 144) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y == 192) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 240) and not (player.rect.x > 48 and player.rect.x < 240 and player.rect.y == 384) and not (player.rect.x > 432 and player.rect.x < 624 and player.rect.y == 384) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 528) and not (player.rect.x > 48 and player.rect.x < 192 and player.rect.y == 624) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 624) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 624):  
        if pressed_keys[K_UP]:
            player.rect.move_ip(0,-1)

    if (player.rect.x >= 48 and player.rect.x <= 624 and player.rect.y < 624) and not (player.rect.x > 48 and player.rect.x < 192 and player.rect.y == 48) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 48) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 48) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 144) and not (player.rect.x > 48 and player.rect.x < 240 and player.rect.y == 288) and not (player.rect.x > 432 and player.rect.x < 624 and player.rect.y == 288) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 432) and not (player.rect.x > 48 and player.rect.x < 144 and player.rect.y == 480) and not (player.rect.x > 96 and player.rect.x < 192 and player.rect.y == 528) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 528) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 528) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y == 480):
            if pressed_keys[K_DOWN]:
                player.rect.move_ip(0, 1)

    if (player.rect.x > 48 and player.rect.y >= 48 and player.rect.y <= 624) and not (player.rect.x == 192 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x == 144 and player.rect.y > 96 and player.rect.y < 192) and not (player.rect.x == 384 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x == 624 and player.rect.y > 48 and player.rect.y < 192) and not (player.rect.x == 432 and player.rect.y > 144 and player.rect.y < 240) and not (player.rect.x == 240 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 624 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 432 and player.rect.y > 432 and player.rect.y < 528) and not (player.rect.x == 144 and player.rect.y > 480 and player.rect.y < 624) and not (player.rect.x == 192 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 384 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 624 and player.rect.y > 480 and player.rect.y < 624):
        if pressed_keys[K_LEFT]:
            player.rect.move_ip(-1, 0)

    if (player.rect.x < 624 and player.rect.y >= 48 and player.rect.y <= 624) and not (player.rect.y > 48 and player.rect.y < 192 and player.rect.x == 48) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y > 96 and player.rect.y < 192) and not (player.rect.x > 240 and player.rect.x < 288 and player.rect.y > 144 and player.rect.y < 240) and not (player.rect.x == 48 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 432 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 240 and player.rect.y > 432 and player.rect.y < 528) and not (player.rect.x == 48 and player.rect.y > 480 and player.rect.y < 624) and not (player.rect.x == 288 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 480 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 528 and player.rect.y > 480 and player.rect.y < 624):
        if pressed_keys[K_RIGHT]:
            player.rect.move_ip(1, 0)

    if pressed_keys[K_SPACE]:
        screen.blit(bomb, (player.rect.left, player.rect.top))
        pygame.display.flip()

    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    draw_walls()
    screen.blit(player.surf, player.rect)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()