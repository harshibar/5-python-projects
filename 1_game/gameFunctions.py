#!/usr/bin/env python
import sys, os, random, pygame
from gameVariables import *

# initialize the game (screen, title, etc)
def initialize_pygame():
    pygame.init()
    pygame.mixer.init()

    # open the window in the center of the screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((screenResolution.current_w - gameWidth) / 2, (screenResolution.current_h - gameHeight) / 2)
    screen = pygame.display.set_mode([gameWidth, gameHeight], pygame.DOUBLEBUF, 32)
    pygame.display.set_icon(pygame.image.load('images/icon.ico'))
    pygame.display.set_caption("Flappy Yogi")

    return screen

# these images will be called in FlappyYogi.py to generate the graphics
def load_images():
    # loading all the images required for the game from the images folder
    # and returning a dictionary of them as following:

    # 'background' : the background
    # 'yogi' : the yogi figure
    # 'yogi2' : the yogi with the tail down
    # 'pipe-up' : the 'pipe' for the upper part, represented by a suspended tennis ball
    # 'pipe-down' : the 'pipe' for the lower part, represented by a fire hydrant
    # 'ground' : the ground

    def load_image(img_file_name):
        # look for images in the game's images folder (./images/)
        # load the image and then converts it, because it speeds up
        # blitting; returning then the image to the dictionary

        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.png'),
            'yogi': load_image('yogi.png'),
            'yogi2': load_image('yogi2.png'),
            'pipe-up': load_image('tennis_ball.png'),
            'pipe-down': load_image('firehydrant.png'),
            'ground': load_image('ground.png')}

# generic method to grab font and wrender text according to coordinates
def draw_text(screen, text, y_pos, size):
    # draw a black text (bigger) and then a white text, smaller
    # over it to get the desired gameScore effect
    font = pygame.font.Font("data/atarian.ttf", size)
    score_text_b = font.render(str(text), 1, (20, 20, 20))
    score_text_w = font.render(str(text), 1, (255, 255, 255))

    x_pos_b = (gameWidth - score_text_b.get_width()) / 2
    x_pos_w = (gameWidth - score_text_w.get_width()) / 2
    screen.blit(score_text_b, (x_pos_b + 2, y_pos - 1))
    screen.blit(score_text_w, (x_pos_w, y_pos))

# does not have any logic, but just gets user input and displays the score,
# fed in from FlappyYogi.py
def end_the_game(screen, gameScore):
    # draw a rectangle & shows the gameScore & updates the highscore
    pygame.draw.rect(screen, (0, 0, 0), (23, gameHeight / 2 - 77, 254, 154))
    pygame.draw.rect(screen, (239, 228, 150), (25, gameHeight / 2 - 75, 250, 150))
    draw_text(screen, "your score: " + str(gameScore), 205, 40)

    f = open("data/highscore", "r+")
    hs = int(f.readline())
    if(gameScore > hs):
       hs = gameScore
       f.seek(0)
       f.truncate()
       f.write(str(hs))
    f.close()

    draw_text(screen, "highscore: " + str(hs), 265, 40)
    draw_text(screen, "press space to restart", 335, 25)
    draw_text(screen, "press esc to exit", 450, 25)

    # update the entire screen for the last time
    pygame.display.update()

    # get the keyboard events to see if the user wants to restart the game
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    return 0
                elif e.key == K_ESCAPE:
                    return 1