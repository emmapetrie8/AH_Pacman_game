#block
import pygame

class Block(pygame.sprite.Sprite):
    """
    This class represents the collectables.

    """
    def __init__(self, filename):
        super().__init__()

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(0,0,0)
        self.rect = self.image.get_rect()
