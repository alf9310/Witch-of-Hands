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
        self.visible_sprites = YSortCameraGroup()
        self.obsticle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self):
        '''
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obsticle_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obsticle_sprites)
        '''
        self.player = Player((2000, 1430), [self.visible_sprites], self.obsticle_sprites)

    def run(self):
        # Update and draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # Camera variables
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Create floor
        self.floor_sur = pygame.image.load('Witch-of-Hands/graphics/tilemap/ground.png').convert()
        self.floor_rec = self.floor_sur.get_rect(topleft = (0, 0))

    def custom_draw(self, player):
        # Get offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw floor
        floor_offset_pos = self.floor_rec.topleft - self.offset
        self.display_surface.blit(self.floor_sur, floor_offset_pos)

        # Sorts by y position for overlays
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            # Camera Offset
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)