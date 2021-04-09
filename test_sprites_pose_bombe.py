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

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

#map_data = [10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 11, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 4, 0, 8, 2, 0, 0, 0, 2, 0, 0, 0, 2, 9, 0, 5, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 4, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 5, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 4, 0, 6, 3, 0, 0, 0, 3, 0, 0, 0, 3, 7, 0, 5, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 12, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 13]

walls_data = [[10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 11], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, 8, 2, -1, -1, -1, 2, -1, -1, -1, 2, 9, -1, 5], [4, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 5], [4, -1, -1, -1, -1, -1, 2, 2, 2, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, 2, 2, 2, -1, -1, -1, -1, -1, 2, 2, 2, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [4, -1, -1, -1, -1, -1, 2, 2, 2, -1, -1, -1, -1, -1, 5], [4, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 5], [4, -1, 6, 3, -1, -1, -1, 3, -1, -1, -1, 3, 7, -1, 5], [4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5], [12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13]]
walls_img_list = []

#ground_data = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 1, -1, -1, 0, -1, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, -1, -1, 0 ,0 ,0, -1, 0, 0, 0, -1, -1, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
#ground_img_list = []

rows = 15
wall_types = 14
#ground_types = 2
tile_size = 48
cols = 15
wall_drawn = False

#for x in range (ground_types):
#    img = pygame.image.load(f'assets/{x}.png')
#    img = pygame.transform.scale(img, (tile_size, tile_size))
#    ground_img_list.append(img)

for x in range (2, wall_types):
    img = pygame.image.load(f'assets/{x}.png')
    img = pygame.transform.scale(img, (tile_size, tile_size))
    walls_img_list.append(img)

top_wall = pygame.Rect(0,0, 720, 33)
bottom_wall = pygame.Rect(0, 672, 720, 48)
left_wall = pygame.Rect(0, 0, 48, 720)
right_wall = pygame.Rect(672, 0, 48, 720)
left_top_corner_wall = [pygame.Rect(96, 96, 96, 48), pygame.Rect(96, 144, 48, 48)]
top_center_tile = pygame.Rect(336, 96, 48, 48)
right_top_corner_wall = [pygame.Rect(528, 96, 96, 48), pygame.Rect(576, 144, 48, 48)]
top_center_wall = pygame.Rect(288, 192, 144, 48)
center_left_wall = pygame.Rect(96, 336, 144, 48)
center_right_wall = pygame.Rect(480, 336, 144, 48)
bottom_center_wall = pygame.Rect(288, 480, 144, 48)
left_bottom_corner_wall = [pygame.Rect(96, 528, 48, 48), pygame.Rect(96, 576, 96, 48)]
bottom_center_tile = pygame.Rect(336, 576, 48, 48)
right_bottom_corner_wall = [pygame.Rect(576, 528, 48, 48), pygame.Rect(528, 576, 96, 48)]

obstacles = [top_wall, bottom_wall, left_wall, right_wall, left_top_corner_wall[0], left_top_corner_wall[1], top_center_tile, right_top_corner_wall[0], right_top_corner_wall[1], top_center_wall, center_left_wall, center_right_wall, bottom_center_wall, left_bottom_corner_wall[0], left_bottom_corner_wall[1], bottom_center_tile, right_bottom_corner_wall[0], right_bottom_corner_wall[1]]

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
        

#walls = pygame.image.load("assets/walls.png").convert_alpha()
#obstacles = walls.get_rect()
#pygame.mask.from_surface(walls)
player = Player("assets/joueur_bleu.png", 200, 200)
bomb = pygame.image.load("assets/bomb.png").convert_alpha()

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

    if player.rect.collidelistall(obstacles):
        print("touching")

    #if player.rect.collidelistall(obstacles) == [] :
    if True: 

        if pressed_keys[K_UP] and pygame.Rect.colliderect(player.rect, top_wall) == False:
            player.rect.move_ip(0,-1)

        if pressed_keys[K_DOWN] and pygame.Rect.colliderect(player.rect, bottom_wall) == False:
            player.rect.move_ip(0, 1)

        if pressed_keys[K_LEFT] and pygame.Rect.colliderect(player.rect, left_wall) == False:
            player.rect.move_ip(-1, 0)
            
        if pressed_keys[K_RIGHT] and pygame.Rect.colliderect(player.rect, right_wall) == False:
            player.rect.move_ip(1, 0)

        if pressed_keys[K_SPACE]:
            screen.blit(bomb, (player.rect.left, player.rect.top))
            pygame.display.flip()

    #if pygame.Rect.colliderect(player.rect, left_corner_wall[0]) or pygame.Rect.colliderect(player.rect, left_corner_wall[1]):
    #    print("touching")
    #if pygame.sprite.collide_mask(player, walls.rect.right):
    #    print("touching right")

    # Fill the screen with white
    

    # Draw the player on the screen

    #if wall_drawn == False:
    #    screen.fill((0, 0, 0))
    #    screen.blit(background, (0,0))
    #    draw_walls()
    #    wall_drawn = True
    #screen.blit(walls, (0,0))
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    draw_walls()
    screen.blit(player.surf, player.rect)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()