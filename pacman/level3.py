#Level3

import pygame
import random
import LevelSuperClass as level
import wall as Wall
import block as Block
BLUE = (0, 0, 255)

class Level3(level):
    #This creates all the walls in level 3
    def __init__(self):
        super().__init__()

                #x,y, X WIDTH, HEIGHT
        walls = [[0, 0, 20, 250, BLUE], #OUTSIDE WALLS
                 [0, 350, 20, 250, BLUE], #OUTSIDE WALLS
                 [780, 0, 20, 250, BLUE], #OUTSIDE WALLS
                 [780, 350, 20, 250, BLUE], #OUTSIDE WALLS
                 [20, 0, 760, 20, BLUE], #OUTSIDE WALLS
                 [20, 580, 760, 20, BLUE], #OUTSIDE WALLS

                 [0, 250, 100, 20, BLUE], #left exit
                 [0, 350, 100, 20, BLUE], #left exit
                 [700, 250, 100, 20, BLUE], #right exit
                 [700, 350, 100, 20, BLUE], #right exit

                 [310, 330, 180, 20, BLUE], #CENTRAL BOX
                 [310, 270, 20, 60, BLUE], #CENTRAL BOX
                 [470, 270, 20, 60, BLUE], #CENTRAL BOX
                 [310, 250, 70, 20, BLUE], #CENTRAL BOX
                 [420, 250, 70, 20, BLUE], #CENTRAL BOX

                 [255, 60, 280, 20, BLUE], #TOP CENTRAL STRIP
                 [390, 60, 20, 100, BLUE], #TOP CENTRAL STRIP
                 [310, 200, 20, 50, BLUE], #STRIPS FROM THE CENTRAL BOX
                 [470, 200, 20, 50, BLUE], #STRIPS FROM THE CENTRAL BOX


                 [255, 520, 280, 20, BLUE], #BOTTOM CENTRAL STRIP
                 [390, 420, 20, 100, BLUE], #BOTTOM CENTRAL STRIP
                 [310, 350, 20, 50, BLUE], #STRIPS FROM THE CENTRAL BOX
                 [470, 350, 20, 50, BLUE], #STRIPS FROM THE CENTRAL BOX

                 [200, 100, 20, 400, BLUE], #LEFT STRIP
                 [570, 100, 20, 400, BLUE], #RIGHT STRIP

                 [60, 60, 20, 100, BLUE], #TOP LEFT BOX
                 [60, 60, 70, 20, BLUE], #TOP LEFT BOX
                 [60, 160, 70, 20, BLUE], #TOP LEFT BOX
                 [130, 60, 20, 120, BLUE], #TOP LEFT BOX

                 [60, 420, 20, 100, BLUE], #BOTTOM LEFT BOX
                 [60, 420, 70, 20, BLUE], #BOTTOM LEFT BOX
                 [60, 520, 90, 20, BLUE], #BOTTOM LEFT BOX
                 [130, 420, 20, 100, BLUE], #BOTTOM LEFT BOX

                 [650, 60, 20, 100, BLUE], #TOP RIGHT BOX
                 [650, 60, 70, 20, BLUE], #TOP RIGHT BOX
                 [650, 160, 70, 20, BLUE], #TOP RIGHT BOX
                 [720, 60, 20, 120, BLUE], #TOP RIGHT BOX

                 [650, 420, 20, 100, BLUE], #BOTTOM RIGHT BOX
                 [650, 420, 70, 20, BLUE], #BOTTOM RIGHT BOX
                 [650, 520, 70, 20, BLUE], #BOTTOM RIGHT BOX
                 [720, 420, 20, 120, BLUE], #BOTTOM RIGHT BOX

                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for i in range(50):
            # This represents the items to be collected
            block = Block("block3.png")

            # Set a random location for the items to be collected
            block.rect.x = random.randrange(100,700)
            block.rect.y = random.randrange(100,500)

            # Add the items to the list of objects
            self.block_list.add(block)



