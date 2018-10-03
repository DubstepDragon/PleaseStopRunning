import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        """Set up a platform"""
        pygame.sprite.Sprite.__init__(self) #Call Parent __init__

        self.image = pygame.Surface((w, h))
        self.image.fill(PLATCOLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

