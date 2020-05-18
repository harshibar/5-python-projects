# im porting libraries
import os, sys, pygame, random, math
from pygame.locals import *

# import functions from other files
from gameFunctions import *
from gameClasses import *
import gameVariables

""" Main method to initialize and run flappy bird game """
def main():
    # initialize pygame & mixer
    screen = initialize_pygame()

    # set up some timers
    clock = pygame.time.Clock()
    pygame.time.set_timer(getNewPipe, pipesAddInterval)

    # load the images, create the bird, ground, and game list
    gamePipes = []

    # this is actually a dog, but it's quite a hassle to rename everything
    gameBird = Bird()
    gameImages = load_images()
    gameVariables.gameScore = 0
    gameGround = Ground(gameImages['ground'])

    # load the game sounds
    jump_sound = pygame.mixer.Sound('sounds/jump.ogg')
    score_sound = pygame.mixer.Sound('sounds/score.ogg')
    dead_sound = pygame.mixer.Sound('sounds/dead.ogg')

    # when the user clicks, the game starts -- wait for that to happen
    while(gameVariables.waitClick == True):
        # draw everything and wait for the user to click to start the game
        # when the user clicks somewhere, the dog will jump and the game will start
        screen.blit(gameImages['background'], (0, 0))
        draw_text(screen, "click to start", 285, 40)
        screen.blit(gameImages['ground'], (0, gameHeight - groundHeight))

        # a new dog is 'drawn' every time it moves
        gameBird.redraw(screen, gameImages['yogi'], gameImages['yogi2'])

        # update the screen
        pygame.display.update()

        # check if the user pressed left click or space and start (or not) the game
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key == K_SPACE):
                gameBird.steps_to_jump = 15
                gameVariables.waitClick = False
    jump_sound.play()

    # loop until the round is over
    while True:
        # draw the background
        screen.blit(gameImages['background'], (0, 0))

        # get the mouse, keyboard or user events and act accordingly
        for e in pygame.event.get():
            # wait for user input
            # different inputs lead to different movements or game actions
            if e.type == getNewPipe:
                # use global variables so game actions are consistent
                p = PipePair(gameWidth, False)
                gamePipes.append(p)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                gameBird.steps_to_jump = jumpSteps
                jump_sound.play()
            elif e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    gameBird.steps_to_jump = jumpSteps
                    jump_sound.play()
                elif e.key == K_ESCAPE:
                    exit()

        # a new frame
        clock.tick(FPS)

        # update the position of the gamePipes and redrawing them; if a pipe is not visible anymore,
        # we remove it from the list
        for p in gamePipes:
            p.x -= pixelsFrame
            # pipe is out of frame, so remove that object (Even if we don't see it)
            if p.x <= - pipeWidth:
                gamePipes.remove(p)
            else:
                screen.blit(gameImages['pipe-up'], (p.x, p.toph))
                screen.blit(gameImages['pipe-down'], (p.x, p.bottomh))

        # every time there's a new frame, redraw everything in the environment (ground, bird, pipe)
        gameGround.move_and_redraw(screen)

        # update the dog position and redrawing it
        gameBird.update_position()
        gameBird.redraw(screen, gameImages['yogi'], gameImages['yogi2'])

        # check for any collisions between the gamePipes, bird and/or the lower and the
        # upper part of the screen

        # a collission occurs when the coordinates of the bird overlap with the pipes
        if any(p.check_collision((gameBird.bird_x, gameBird.bird_y)) for p in gamePipes) or \
               gameBird.bird_y < 0 or \
               gameBird.bird_y + birdHeight > gameHeight - groundHeight:
            dead_sound.play()
            break

        # there were no collision if we ended up here, so we are checking to see if
        # the dog went thourgh one half of the pipe's gameWidth; if so, we update the gameScore
        for p in gamePipes:
            if(gameBird.bird_x > p.x and not p.score_counted):
                p.score_counted = True
                # increment global gameScore
                gameVariables.gameScore += 1
                score_sound.play()

        # draw the gameScore on the screen
        draw_text(screen, gameVariables.gameScore, 50, 50)
        pygame.display.update()

    # make the dog 'fall' if the round is over
    while(gameBird.bird_y + birdHeight < gameHeight - groundHeight):
        # redraw the background
        screen.blit(gameImages['background'], (0, 0))

        # redraw the gamePipes in the same place as when it died
        for p in gamePipes:
            screen.blit(gameImages['pipe-up'], (p.x, p.toph))
            screen.blit(gameImages['pipe-down'], (p.x, p.bottomh))

        # draw the ground piece to get the rolling effect
        gameGround.move_and_redraw(screen)

        # make the dog fall down and rotates it
        gameBird.redraw_dead(screen, gameImages['yogi'])

        # one more tick
        clock.tick(FPS * 3)

        # update the entire screen
        pygame.display.update()

    # end the game?
    if not end_the_game(screen, gameVariables.gameScore):
        main()
    else:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()
