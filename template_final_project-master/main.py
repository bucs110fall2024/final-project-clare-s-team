import pygame 
from src.controller import Controller 
SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 550 
def main():
    pygame.init() 
    controller = Controller(SCREEN_WIDTH, SCREEN_HEIGHT) 
    controller.mainloop()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main() 