import pygame 
from src import Controller 
#import your controller             from src.controller import controller 
SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 550 
KEY_HEIGHT = 250 
KEY_WIDTH = 100 
def main():
    pygame.init() 
    controller = Controller.Controller(SCREEN_WIDTH, SCREEN_HEIGHT) 
    controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main() 