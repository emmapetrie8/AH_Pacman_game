import pygame
import random

# Call this function so the Pygame library can initialize itself
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

font = pygame.font.Font(None, 36)

popSound = pygame.mixer.Sound("GhostCollide.wav")
gameOver = pygame.mixer.Sound("GameOver.wav")
movingPacman = pygame.mixer.Sound("moving.wav")
collectingBlocks = pygame.mixer.Sound("eatingBlocks.wav")

levelNumber = 1

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite):
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
        self.image = pygame.Surface([20, 25])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.image.blit(pygame.image.load("PACMAN1.png"), (0,0))

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

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

class Block(pygame.sprite.Sprite):
    """
    This class represents the collectables.

    """
    def __init__(self, filename):
        super().__init__()

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class level(object):
    """ Base class for all levels. """

    # Each level has a list of walls, and of blocks.
    wall_list = None

    block_list = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()

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

def main():
    """ Main Program """

    #tells the program to use the global variable, instead of making a new one
    global levelNumber


    lives = 3

    # Create an 800x600 sized screen
    ScreenWidth = 800
    ScreenHeight = 600
    screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])


    # Set the title of the window
    pygame.display.set_caption('Pac-Man')

    # Create the player paddle object
    player = Player(400,300)
    ghost1 = Ghost(50,50)
    ghost2 = Ghost(700, 50)
    ghost3 = Ghost(700, 550)
    ghost4 = Ghost(50, 550)

    ghost_list = pygame.sprite.Group()
    ghost_list.add(ghost1)
    ghost_list.add(ghost2)
    ghost_list.add(ghost3)
    ghost_list.add(ghost4)

    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    movingsprites.add(ghost1)
    movingsprites.add(ghost2)
    movingsprites.add(ghost3)
    movingsprites.add(ghost4)

    # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    score = 0

    Levels = []

    level = Level1()
    Levels.append(level)

    level = Level2()
    Levels.append(level)

    level = Level3()
    Levels.append(level)


    current_level_no = 0
    current_level = Levels[current_level_no]

    clock = pygame.time.Clock()

    done = False

    while not done:
        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                    movingPacman.play()
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                    movingPacman.play()
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                    movingPacman.play()
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                    movingPacman.play()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                    movingPacman.play()
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                    movingPacman.play()
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                    movingPacman.play()
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                    movingPacman.play()

        # --- Game Logic ---

        player.move(current_level.wall_list)
        ghost1.move(player.rect.x,player.rect.y)
        ghost2.move(player.rect.x,player.rect.y)
        ghost3.move(player.rect.x,player.rect.y)
        ghost4.move(player.rect.x,player.rect.y)


        if player.rect.x <-15:
            player.rect.x = 800

        if player.rect.x >800:
            player.rect.x = -15


        #checks if the ghosts are on top or eachother, and if so resets ghost1's coordinates
        if ghost1.rect.x == ghost2.rect.x and ghost1.rect.y == ghost2.rect.y:
            ghost1.rect.x = (50)
            ghost1.rect.y = (50)

        if ghost1.rect.x == ghost3.rect.x and ghost1.rect.y == ghost3.rect.y:
            ghost1.rect.x = (50)
            ghost1.rect.y = (50)

        if ghost1.rect.x == ghost4.rect.x and ghost1.rect.y == ghost4.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost2.rect.x == ghost1.rect.x and ghost2.rect.y == ghost1.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost2.rect.x == ghost3.rect.x and ghost2.rect.y == ghost3.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost2.rect.x == ghost4.rect.x and ghost2.rect.y == ghost4.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost3.rect.x == ghost1.rect.x and ghost3.rect.y == ghost1.rect.y:
            ghost3.rect.x = (700)
            ghost3.rect.y = (550)
        
        if ghost3.rect.x == ghost2.rect.x and ghost3.rect.y == ghost2.rect.y:
            ghost3.rect.x = (700)
            ghost3.rect.y = (550)
        
        if ghost3.rect.x == ghost4.rect.x and ghost3.rect.y == ghost4.rect.y:
            ghost3.rect.x = (700)
            ghost3.rect.y = (550)
        
        if ghost4.rect.x == ghost1.rect.x and ghost4.rect.y == ghost1.rect.y:
            ghost4.rect.x = (50)
            ghost4.rect.y = (550)
        
        if ghost4.rect.x == ghost2.rect.x and ghost4.rect.y == ghost2.rect.y:
            ghost4.rect.x = (50)
            ghost4.rect.y = (550)

        if ghost4.rect.x == ghost3.rect.x and ghost4.rect.y == ghost3.rect.y:
            ghost4.rect.x = (50)
            ghost4.rect.y = (550)


        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, current_level.block_list, True)

        if len(blocks_hit_list) >0:
            collectingBlocks.play()


        #see if the ghost has collided with the player
        ghost_hit_list = pygame.sprite.spritecollide(player, ghost_list, False)

        #checks if the ghost has collided with the player and if so takes away a life
        #and resets the ghosts position
        if len(ghost_hit_list) > 0:
            lives -= 1
            popSound.play()
            ghost1.rect.x = 50
            ghost1.rect.y = 50
            ghost2.rect.x = 700
            ghost2.rect.y = 50
            ghost3.rect.x = 700
            ghost3.rect.y = 550
            ghost4.rect.x = 50
            ghost4.rect.y = 550


        # Check the list of collisions.
        for block in blocks_hit_list:
            score += 1

        if score == 40:
            levelNumber = 2
            current_level_no = 1
            current_level = Levels[current_level_no]

        if score == 80:
            levelNumber = 3
            current_level_no = 2
            current_level = Levels[current_level_no]

        if score == 110:
            screenGameOver = font.render(str("Game completed!"), 1, BLACK)
            screen.fill(GREEN)
            #MAKES THE FINAL SCORE THE NUMBER OF BLOCKS COLLECTED TIMES BY THE NUMBER OF LIVES LEFT
            finalScore = score * lives
            ScreenScore = font.render(str(score), 1, BLACK)
            screen.blit(screenGameOver, (300,300))
            screen.blit(ScreenScore, (400, 400))
            pygame.display.flip()
            clock.tick(40)
            pygame.time.wait(200)

        if lives == 0:
            gameOver.play()
            finalScore = score * lives
            LivesDoneScreen = font.render(str("You've been caught by the ghost"), 1, WHITE)
            screen.blit(LivesDoneScreen, (300, 300))
            ScreenScoreGhost = font.render(str(finalScore), 1, WHITE)
            screen.blit(ScreenScoreGhost, (400, 400))
            screen.fill(RED)

            pygame.display.flip()
            done = True
            clock.tick(40)
            pygame.time.wait(500)


        # --- Drawing ---
        screen.fill(BLACK)


        current_level.wall_list.draw(screen)
        current_level.block_list.draw(screen)
         #Draw all the spites
        all_sprites_list.draw(screen)
        #all_block_list.draw(screen)
        movingsprites.draw(screen)

        textLevelDisplay = font.render("Level " + str(levelNumber), 1, WHITE)
        textImg = font.render(str (textLevelDisplay),1,WHITE)
        screen.blit( textLevelDisplay, (20,20) )

        textImg = font.render("score:" + str (score),1,WHITE)
        screen.blit( textImg, (20,40) )

        textImg = font.render("lives: " + (str(lives)),1,WHITE)
        screen.blit( textImg, (20, 60))


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()