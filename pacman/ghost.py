#ghost
import pygame
class Ghost(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([20,25])
        self.image = pygame.image.load("ghost1.jpg")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



    def move(self,pacX,pacY):
        """ Find the position of the player and chase them """
        if pacX > self.rect.x:
        # Move left/right
            self.rect.x += 1
        else:
            self.rect.x -= 1

        if pacY > self.rect.y:
            self.rect.y += 1
        else:
            self.rect.y -= 1
