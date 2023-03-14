import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obsticle_sprites):
        super().__init__(groups)
        # Sprite
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        # Collisions 
        self.obsticle_sprites = obsticle_sprites

    def input(self):
        # Movement
        # TODO add mediapipe directional inputs
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, speed):
        # Same speed in all directions
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # Movement split up for collisions 
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obsticle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # Moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # Moving left
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obsticle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # Moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # Moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)