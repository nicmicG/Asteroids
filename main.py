#imports pygame package
import pygame

#import all values from constants.py
from constants import *

#import Player class from player.py
from player import Player

def main():
    #initialize pygame and values
    pygame.init()

    #create pygame clock
    clock = pygame.time.Clock()
    #create dt variable
    dt = 0

    #instantiate player ship object, assign to Player1 variable
    Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #create a screen with the width and height from constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #display startup text
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")


    

#set parameter for game loop
    running = True
#create loop to draw game screen
    while running == True:
        #quit game if pygame.QUIT occurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #update player object before rendering
        Player1.update(dt)

        #fill the screen with black color
        screen.fill("black")

        

        #use player1 variable and .draw(screen) to draw the player ship
        Player1.draw(screen)


        #update the display
        pygame.display.flip()

        #pause the game loop for 1/60 of a second
        #this is to make the game run at 60 frames per second
        #additionally, update dt variable
        dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds


#runs only if this file is run directly
#this allows us to import this file without running the main function
if __name__ == "__main__":
   main()