#level1
import pygame
import random
import LevelSuperClass as level
import wall as Wall
import block as Block
BLUE = (0, 0, 255)

class Level1(level):
    """This creates all the walls in level 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLUE], # outside wall
                 [0, 350, 20, 250, BLUE], # outside wall
                 [780, 0, 20, 250, BLUE], # outside wall
                 [780, 350, 20, 250, BLUE], # outside wall
                 [20, 0, 760, 20, BLUE], # outside wall
                 [20, 580, 760, 20, BLUE], # outside wall

                 [310, 330, 180, 20, BLUE], #CENTRAL BOX
                 [310, 270, 20, 60, BLUE], #CENTRAL BOX
                 [470, 270, 20, 60, BLUE], #CENTRAL BOX
                 [310, 250, 70, 20, BLUE], #CENTRAL BOX
                 [420, 250, 70, 20, BLUE], #CENTRAL BOX

                 [0, 250, 100, 20, BLUE], #left exit
                 [0, 350, 100, 20, BLUE], #left exit
                 [700, 250, 100, 20, BLUE], #right exit
                 [700, 350, 100, 20, BLUE], #right exit

                 [310, 130, 180, 20, BLUE], #T above central box
                 [390, 130, 20, 70, BLUE], #T above central box

                 [200, 200, 20, 200, BLUE], #STRIP BESIDE LEFT EXIT
                 [590, 200, 20, 200, BLUE], #STRIP BESIDE RIGHT EXIT

                 [80, 80, 120, 20, BLUE], #TOP LEFT BOX top
                 [80, 100, 20, 50, BLUE], #TOP LEFT BOX side left
                 [200, 80, 20, 80, BLUE], #TOP LEFT BOX side right
                 [80, 140, 120, 20, BLUE], #TOP LEFT BOX bottom

                 [580, 80, 120,20, BLUE], #TOP RIGHT BOX top
                 [580, 100, 20, 50, BLUE], #TOP RIGHT BOX side left
                 [580, 140, 120, 20, BLUE], #TOP RIGHT BOX bottom
                 [700, 80, 20, 80, BLUE], #TOP RIGHT BOX side right


                 [390, 0, 20, 100, BLUE], #TOP CENTRAL STRIP
                 [390, 500, 20, 100, BLUE], #BOTTOM CENTRAL T
                 [310, 480, 180, 20, BLUE], #BOTTOM CENTRAL T

                 [80, 520, 120, 20, BLUE], #BOTTOM LEFT BOX bottom
                 [80, 460, 120, 20, BLUE], #BOTTOM LEFT BOX top
                 [80, 460, 20, 80, BLUE], #BOTTOM LEFT BOX left side
                 [200, 460, 20, 80, BLUE], #BOTTOM LEFT BOX right side

                 [580, 520, 120, 20, BLUE], #BOTTOM RIGHT BOX top
                 [580, 460, 120, 20, BLUE],#BOTTOM RIGHT BOX bottom
                 [580, 460, 20, 80, BLUE], #BOTTOM RIGHT BOX left side
                 [700, 460, 20, 80, BLUE], #BOTTOM RIGHT BOX right side

                ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for i in range(50):
            # This represents the items to be collected
            block = Block("block.png")

            # Set a random location for the items to be collected
            block.rect.x = random.randrange(100,700)
            block.rect.y = random.randrange(100,500)

            # Add the items to the list of objects
            self.block_list.add(block)
