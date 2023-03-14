''' Main Game Module for Witch of Hands '''
__author__ = "Audrey Fuller"
__credits__ = ["RPG framework: Clear Code"]

import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):
        # Setup pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Witch of Hands')
        # TODO create iconpygame.display.set_icon(pygame.image.load('../graphics/test/rock.png'))
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        # Event Loop
        while True:
            for event in pygame.event.get():
                # Exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()