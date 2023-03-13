import pygame

class Level:
    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.obsticle_sprites = pygame.sprite.Group()

    def run(self):
        # Update and draw game
        pass