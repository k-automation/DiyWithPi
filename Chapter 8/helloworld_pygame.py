# Snakey (A Nibbles Clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com
# Creative Commons BY-NC-SA license
# 158 lines of code


"""
Welcome to the Code Comments for Snakey. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/

HOW TO PLAY SNAKEY:
You are the green snake on the screen. Use the arrow keys or the WASD keys to move the snake around and eat the red apples that are on the screen. Each time you eat an apply, your snake grows in length. Do not run into either the edges or yourself.
"""

import random
import time
import pygame
import sys
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
"""

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.

For example, if we used 20 instead of CELLSIZE, then if we wanted to change our code later we'd have to change every place in the code we find 20. This is trickier than just changing the one line where CELLSIZE is originally set.

Note that WINDOWWIDTH and WINDOWHEIGHT refer to the width and height of the game window in pixels. We'll further divide up the window into "cells", which are areas that each segment of the snake and the apple can exist in. The window will be CELLWIDTH cells in width and CELLHEIGHT cells in height, with each CELLSIZE set to 20 pixels.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)

BGCOLOR = BLACK
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

"""We need values for each of the directions up, down, left, and right in our program. These can be any four distinct values, as long as they are used consistently it won't matter to our program. We could use the strings 'up', 'down', etc. Instead, we'll use constant variables.

The difference is if we make a typo using the strings, Python won't crash but it will still cause a bug. For instance, if we had this bit of code:
    if direction == 'dwon':
...then the program will still run, but it would contain a bug because if the direction variable was set to 'down', this condition would still evaluate to False (which is not how we'd want the code to behave).

But if we use constant values instead and make a similar typo:
    if direction == DWON:
...then Python crashes when it comes across this line because there is no such variable as DWON, just DOWN. Why is crashing a good thing? Well, it's not, but in this case it would immediately alert us that there is a problem, and we could fix it. If we had used a string instead, it might take a while to track down where the bug is caused. Using constants in this way helps us ensure that our program works correctly.
"""

def main():
    global MAINCLOCK, MAINSURF, BASICFONT
    """The main() function is where our program begins. (See the last two lines of code to see why.) Normally, because we define MAINCLOCK and MAINSURF and BASICFONT inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF and BASICFONT won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snakey')
    """pygame.init() needs to be called before any of the other Pygame functions.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 15 frames per second (or whatever integer value we have in the FPS constant.)

    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().

    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions

    The call to the pygame.font.Font() constructor function creates a Font object. We will store this Font object in the global variable BASICFONT."""

    showStartScreen()
    while True:
        gameLoop()
        showGameOverScreen()
    """The animation of the rotating "Snakey!" text is handling inside the showStartScreen() function and will be explained later. After the call to showStartScreen() returns, we enter an infinite loop where the main part of the game is run (in the gameLoop() function) and then the "game over" screen is show (in the showGameOverScreen() function) when the game ends. Because this loop keeps looping, the game starts again after the showGameOverScreen() is done."""

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    """There are six steps to making text display on the screen in Pygame. The first is to create a pygame.font.Font object (which we will just call a Font object for short). In this case, we create a Font object from the "freesansbold.ttf" font file (this font comes with Pygame) and we want the size of the Font to be at 100 points.

    If you want to draw text in other fonts or sizes, you must create a new Font object for each one."""

    titleSurf1 = titleFont.render('Snakey!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snakey!', True, GREEN)
    pressKeySurf = BASICFONT.render('Press a key to start.', True, DARKGRAY)
    """The second step is to call the Font object's render() method, which will return a Surface object with the text drawn on it. The fourth parameter provides the background color on the Surface. If you don't provide this fourth parameter, then the Surface object will have a transparent background.

    There is more info on anti-aliasing at http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects

    Remember that the font size information is already stored in the pygame.font object stored in our global variable named FONT.
    """

    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    """The third step is to get a Rect object from the Surface object, so we can set the position of the text on the screen. The Surface object's get_rect() method will return a Rect object for the surface with the text on it.

    The fourth step is to set the position of the text. You can see the above two lines are getting the Rect object for the "Press a key to start." and then setting the topleft corner of the Rect to an x coordinate of WINDOWWIDTH - 200 (that is, 200 pixels to the left of the window's right edge (since the window is WINDOWWIDTH pixels long)) and a y coordinate of WINDOWHEIGHT - 30.

    The fifth step is to draw the Surface object containing the text at the position on the screen specified by the Rect object with the blit() method. The sixth step is to call pygame.display.update(). These are done a few lines down.
    """

    degrees1 = 0
    degrees2 = 0
    while True:
        """To achieve the rotating "Snakey!" animation in the game's start menu, we will take the Surface objects stored in titleSurf1 and titleSurf2, and create rotated images of them (which will be stored in Surface objects in the rotatedSurf1 and rotatedSurf2 variables). We will rotate them at larger and larger amounts of rotation each time we draw them on the screen, so it looks like they're spinning around until they circle all the way aroud.

        The degrees1 and degrees2 will track how many degrees we rotate the two pieces of text."""

        MAINSURF.fill(BGCOLOR)
        """To wipe out the previous screen, first we fill MAINSURF will the background color we stored in BGCOLOR. Remember, the Surface object stored in MAINSURF is special because it was the Surface object returned by pygame.display.set_mode(), which means that what is drawn on this Surface object will appear on the screen when the pygame.display.update() function is called. All the other Surface objects just exist in the computer's memory and won't be displayed on the screen unless they are copied to MAINSURF with the blit() method."""

        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        """Creating a new rotated surface from another surface object is easy to do. Just call the pygame.transform.rotate() function, passing the Surface object you want to get a rotated Surface object of for the first parameter (like we do with titleSurf1 above), and then pass an integer of how many degrees you want it rotated.

        There are 360 degrees in one full rotation, and in Pygame a positive integer for rotating will rotate the image counterclockwise, and a negative integer will rotate the image clockwise.

        Note that the original Surface object stored in the titleSurf1 is not rotated, but rather a copy of titleSurf1 is made and returned by pygame.transform.rotate() and it is that Surface object that is rotated."""

        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        """Now (just like the third and fourth step we took with pressKeySurf above), we want to get a Rect object from the Surface object in rotatedSurf1 so we can position it."""

        MAINSURF.blit(rotatedSurf1, rotatedRect1)
        """Here is the fifth step in getting text to appear on the screen: calling the Surface object's blit() method (in this case, the Surface object is the one in MAINSURF) so that we can copy the rotated surface to MAINSURF."""

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        MAINSURF.blit(rotatedSurf2, rotatedRect2)
        """Here we do the same rotate/get the Rect/set the position/blit to MAINSURF steps with titleSurf2."""

        MAINSURF.blit(pressKeySurf, pressKeyRect)
        """We'll also blit the "Press a key to start." text to the screen."""

        if checkForKeyPress():
            return
        """Rememeber that this code is currently in an infinite loop, and will repeat until the program execution reaches a break or return statement. Here, we call our checkForKeyPress() function (which we will define later) to see if the user has pressed any key. If this function returns True, then we execute a return statement and break out of showStartScreen()."""

        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """The call to pygame.display.update() takes everything drawn on the MAINSURF surface and draws it on the screen. The call to MAINCLOCK.tick() will then cause the program to wait for a fraction of a second. If we didn't have this call, then the program would draw frames of this animation as fast as possible. This means our game would run very fast on fast computers, and very slow on slow computers."""

        degrees1 += 3
        degrees2 += 7
        if degrees1 > 360:
            degrees1 -= 360
        if degrees2 > 360:
            degrees2 -= 360
        """For the next frame of animation, we want to rotate the two "Snakey!" pieces of text at different rates. So we increase degrees1 by 3 while we increase degrees2 by 7. Just to ensure that these values don't get too large, if they get above 360 we will subtract 360 from them."""


def checkForKeyPress():
    """This function will look at the event queue for any key press events and return the first one it finds. It also checks if the program is trying to quit, in which case, it calls terminate() to end the program.

    You can also call this function and ignore the return value if you just want to pause the program until the user presses a key."""
    for event in pygame.event.get(QUIT):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        return event.key


def terminate():
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library."""
    pygame.quit()
    sys.exit()


def gameLoop():
    """This is where the main part of the game takes place. We have an infinite loop (the "while True:" loop) that handles player input, updating the state of the game world, and displaying the game world on the screen. The part before the infinite loop sets up variables for the start of a game. When the game is over, we return from this function."""

    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [(startx, starty), (startx-1, starty)]
    """The data structure that we will use to keep track of the snake is a list of tuples of two integers. Each tuple represents one segment of the snake. The two integers represent the x & y coordinates of the snake segment. The snake starts off with two segments at a random location."""

    direction = RIGHT
    """At the start of the game, we'll just have the snake be going to the RIGHT."""

    apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
    """We'll start the first apple off at a random location on the screen."""

    while True:
        # get player input
        for event in pygame.event.get():
            """Here we loop through all the events in the event queue. The pygame.event.get() function will return a list of pygame.event.Event objects that have been generated since the last time pygame.event.get() was called. An Event object is generated whenever the player presses a key, clicks the mouse, tries to shut down the program, move sthe mouse, and many other situations.

            More info on events can be found here: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent
            """

            if event.type == QUIT:
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means. Note that QUIT comes from pygame.locals.QUIT, but we can simply type QUIT because we used "from pygame.locals import *" instead of "import pygame.locals". The same applies for MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, and the keyboard constants such as K_ESCAPE and K_8 since these values are also in pygame.locals."""
                terminate()
            elif event.type == KEYDOWN:
                """The KEYDOWN event is created when the user presses any key on the keyboard. We can tell which key the user pressed by looking at the value in event.key

                By pressing one of the keys, we will change the value in the direction variable so that the snake heads in a new direction. The player can either use the arrow keys (whose value in Pygame is represented by Pygame's K_LEFT and K_DOWN (etc) constants), or by using the WASD keys (which are for up, left, down, and right respectively.) We use Pygame's K_a and K_w (etc) constants for those keys.

                Also note that we don't want the snake to be able to turn in on itself and end the game. So if the snake is going right but the player pushes the left arrow key, we don't want to change the value in the direction variable."""
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                if event.key == K_ESCAPE:
                    """If the player pushes the Esc key, then we want to terminate the program."""
                    terminate()

        # check if the snake has hit itself or the edge
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
            """The condition in this if statement checks if the head of the snake (which will always be the tuple in snakeCoords[0]) has gone past the edge. If does this by checking if the head's x coordinate (which is at snakeCoords[0][0]) has a value of -1 or CELLWIDTH or if the head's y coordinate (which is at snakeCoords[0][1]) has a value of -1 or CELLHEIGHT.

            The reason we check if the coordinate is at CELLWIDTH or CELLHEIGHT instead of CELLWIDTH+1 or CELLHEIGHT+1 is because the cells on the window start at 0, not at 1. Say if CELLWIDTH was 32. This means the cells go from 0 to 31, not 1 to 32. So the cell x coordinate 32 would be the one just past the right edge of the screen."""
            return
        for snakeBody in snakeCoords[1:]:
            """In this for loop, we check if the snake's head (snakeCoords[0]) is in the same location as any of the other segments of the snake. This will tell us if the snake has crashed into itself or not.

            So this for loop will loop over each tuple in snakeCoords except for the first one. This is because we are using snakeCoords[1:], which means the list of values in the list starting with the one at index 1 (which is the second value, since the first index is 0). We don't want to see if the snake head is in the same location as the snake head, because this would always be true and cause an immediate game over that the player could never avoid."""
            if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                return

        """The snake "moves" by constantly adding another tuple to the front of the snakeCoords list, with x and y coordinates that make it expand in the direction dictated by the "direction" variable. Adding this segment makes the snake grow by one segment. To give the appearance of movement, we then remove the last tuple in the list, which makes the snake appear to shrink by one segment. This is what causes the snake to "move" around the board.

        When the snake eats an apple, we just skip removing the last tuple from the list. The net effect is that the snake is ends up being one segment longer than it was."""

        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            """If the snake's head is at the same location as the apple, then we immediately want to set the location of the apple to a new location. This will make the apple at the old location disappear, making it look like the snake "ate" the apple. Growing the snake by one segment is handled later."""
            apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
        else:
            snakeCoords.pop()
            """The pop() list method removes the last value in a list. This makes the last "tail" segment of the snake disappear."""

        # move the snake
        """Here we insert a new tuple to the snakeCoords list, with xy coordinates that depend on the value in the variable named direction."""
        if direction == UP:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] - 1))
        elif direction == DOWN:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] + 1))
        elif direction == LEFT:
            snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        elif direction == RIGHT:
            snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))

        """Now that we're done with all the logic, we just want to draw the background, snake, apple, and score on the screen."""
        MAINSURF.fill(BGCOLOR)
        drawSnake(snakeCoords)
        drawApple(apple)
        drawScore(len(snakeCoords))
        """Note that the score is equal to how many segments are in the snake, which is equal to the number of tuples in the snakeCoords list."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """Then we call pygame.display.update() to update the screen, and call MAINCLOCK.tick(FPS) to pause the program a little bit so the game doesn't run too fast."""


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    MAINSURF.blit(gameSurf, gameRect)
    MAINSURF.blit(overSurf, overRect)
    pygame.display.update()
    """Here we create a new Font object with big, 150 point letters. Then we render two surfaces with "Game" and "Over" and then display them on the screen."""

    time.sleep(0.5)
    checkForKeyPress() # clear out any key presses in the event queue made up to this point
    """Because the next game will start immediately after we exit out of this loop, we want the "Game Over" text to stay on the screen for at least half a second. Then we also want to clear out all the key press events from the event queue. This will keep the player from accidentally skipping past the Game Over screen and starting the next game too soon because they pressed a key while the last game was still going on."""

    """Now we enter an infinite loop that only returns from this function when the user has pressed a key."""
    while True:
        if checkForKeyPress():
            return


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 80, 10)
    MAINSURF.blit(scoreSurf, scoreRect)
    """The drawScore() function simply displays the score."""


def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        coordRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(MAINSURF, GREEN, coordRect)
        """This code loops through each of the tuples in snakeCoords and draws a green square on the screen using the pygame.draw.rect() function. This is how we make the snake appear on the screen. Remember though, the MAINSURF surface won't appear on the screen until the pygame.display.update() function is called. (This is done at the end of the gameLoop() function."""

def drawApple(coord):
    x = coord[0] * CELLSIZE
    y = coord[1] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(MAINSURF, RED, appleRect)
    """This function is very similar to the drawSnake() function, except there is no list that needs to be iterated over. And it draws a red square for the apple, instead of a green one."""


if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program (aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name snakey.py, then the __name__ variable will contain 'snakey').

    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import snakey" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse."""

