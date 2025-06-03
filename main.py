#imports pygame package
import pygame

#import all values from constants.py
from constants import *

def main():
#initialize pygame
    pygame.init()
#startup text
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

#create a screen with the width and height from constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#initialize the game loop
    running = True
#create loop to draw game screen
    while running == True:
        #quit game if pygame.QUIT occurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill the screen with black color
        screen.fill("black")
        #update the display
        pygame.display.flip()



#runs only if this file is run directly
#this allows us to import this file without running the main function
if __name__ == "__main__":
   main()