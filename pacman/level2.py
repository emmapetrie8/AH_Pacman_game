#Level2
import pygame
import random
import LevelSuperClass as level
import wall as Wall
import block as Block
BLUE = (0, 0, 255)

class Level2(level):
    #This creates all the walls in level 2
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, BLUE], #outer wall
                 [0, 350, 20, 250, BLUE], #outer wall
                 [780, 0, 20, 250, BLUE], #outer wall
                 [780, 350, 20, 250, BLUE], #outer wall
                 [20, 0, 760, 20, BLUE], #outer wall
                 [20, 580, 760, 20, BLUE], #outer wall

                 [200, 50, 150, 20, BLUE], #TOP LEFT STRIP
                 [450, 50, 150, 20, BLUE], #TOP RIGHT STRIP
                 [200, 525, 150, 20, BLUE], #BOTTOM LEFT STRIP
                 [450, 525, 150, 20, BLUE], #BOTTOM RIGHT STRIP

                 [0, 250, 100, 20, BLUE], #left exit
                 [0, 350, 100, 20, BLUE], #left exit
                 [700, 250, 100, 20, BLUE], #right exit
                 [700, 350, 100, 20, BLUE], #right exit

                 [310, 330, 180, 20, BLUE], #CENTRAL BOX
                 [310, 270, 20, 60, BLUE], #CENTRAL BOX
                 [470, 270, 20, 60, BLUE], #CENTRAL BOX
                 [310, 250, 70, 20, BLUE], #CENTRAL BOX
                 [420, 250, 70, 20, BLUE], #CENTRAL BOX

                 [310, 130, 180, 20, BLUE], #T above central box
                 [390, 130, 20, 70, BLUE], #T above central box

                 [200, 180, 20, 100, BLUE], #STRIPS BESIDE LEFT EXIT
                 [200, 320, 20, 100, BLUE], #STRIPS BESIDE LEFT EXIT
                 [590, 180, 20, 100, BLUE], #STRIPS BESIDE RIGHT EXIT
                 [590, 320, 20, 100, BLUE], #STRIPS BESIDE RIGHT EXIT

                 [100, 50, 20, 150, BLUE], #TOP LEFT T
                 [100, 110, 75, 20, BLUE], #TOP LEFT T

                 [700, 50, 20, 150, BLUE], #TOP RIGHT T
                 [645, 110, 60, 20, BLUE], #TOP RIGHT T

                 [100, 405, 20, 130, BLUE], #BOTTOM LEFT T
                 [100, 460, 75, 20, BLUE], #BOTTOM LEFT T

                 [700, 405, 20, 130, BLUE], #BOTTOM RIGHT T
                 [645, 460, 75, 20, BLUE], #BOTTOM RIGHT T

                 [310, 425, 180, 20, BLUE], #STRIP BELLOW CENTRAL BOX
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for i in range(50):
            # This represents the items to be collected
            block = Block("block2.png")

            # Set a random location for the items to be collected
            block.rect.x = random.randrange(100,700)
            block.rect.y = random.randrange(100,500)

            # Add the items to the list of objects
            self.block_list.add(block)