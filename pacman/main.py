#main game 
import pygame
import random
import Player
import wall
import ghost as Ghost
import level1 as Level1
import level2 as Level2
import level3 as Level3


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

        if ghost2.rect.x == ghost3.rect.x and ghost2.rect.y == ghost3.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost2.rect.x == ghost4.rect.x and ghost2.rect.y == ghost4.rect.y:
            ghost2.rect.x = (700)
            ghost2.rect.y = (50)

        if ghost3.rect.x == ghost4.rect.x and ghost3.rect.y == ghost4.rect.y:
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