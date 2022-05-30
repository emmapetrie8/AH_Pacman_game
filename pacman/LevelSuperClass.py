#level super class
import pygame

class level(object):
    """ Base class for all levels. """

    # Each level has a list of walls, and of blocks.
    wall_list = None

    block_list = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
