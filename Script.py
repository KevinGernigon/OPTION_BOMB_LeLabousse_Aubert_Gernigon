import pygame
from pygame.locals import *

from pytmx.util_pygame import load_pygame

def blit_all_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            #tile[0] .... x grid location
            #tile[1] .... y grid location
            #tile[2] .... image data for blitting
            img = pygame.transform.scale(tile[2],(32,32))
            x_pixel = tile [0] * 32 + world_offset[0]
            y_pixel = tile [1] * 32 + world_offset[1]
            window.blit( tile[2], (x_pixel, y_pixel))

def main():
    tmxdata = load_pygame("LaCarte.tmx")
    quit = False
    world_offset = [0,0]

    while not quit:
        window.fill((64,64,64))
        blit_all_tiles(window,tmxdata,world_offset)
        for event in pygame.event.get():
            if event.type ==  QUIT:
                quit = True