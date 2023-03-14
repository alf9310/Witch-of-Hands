import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.obsticle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obsticle_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obsticle_sprites)


    def run(self):
        # Update and draw game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)