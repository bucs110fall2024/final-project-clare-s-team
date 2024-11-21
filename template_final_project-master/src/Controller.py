import pygame 
from src.model_a import Keys 
from src. model_b import Music 
class Controller: 
  
  def __init__(self): 
    """
        Initializes the controller
        args: None 
        return: None 
        """ 
    #setup pygame data
    pygame.init()
    pygame.event.pump() 
    self.screen = pygame.display.set_mode()            #Full screen 
    #self.k1 = Key() 
    #self.k2 = Key() 
    
  def mainloop(self): 
    """
        Includes procedures that need to continue throughout the entirety of the game 
        args: 
            - x (int): starting x coordinate 
            - y (int): starting y coordinate 
            - img_file (str): path to img file 
        """ 
    #select state loop
    while True: 
      #1. Event 
      for event in pygame.events.get(): 
        if event.type == pygame.QUIT: 
          pygame.quit() 
          exit() 
      #2. Update 
      #3. Redraw 
        #self.clouds.draw() 
        #self.background = pygame.image.load("assets/background.png") 
        #self.screen.blit(slef.background, (0,0)) 
      #4. Display 
    
  
  ### below are some sample loop states ###

  def menuloop(self): 
    """
    Manages menu screen and its interactive buttons  
      args: None 
      return: None 
    """ 
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self): 
    """
    Manages game and includes the interactive piano keys and music notes 
      args: None 
      return: None 
    """ 
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self): 
    """
    Changes screen when previous song played is over and displays other song options for another song 
      args: None 
      return: None 
    """ 
      #event loop

      #update data

      #redraw
