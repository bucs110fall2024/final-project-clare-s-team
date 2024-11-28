import pygame
import pygame.freetype 
from src.keys import Keys 
from src.buttons import Buttons 
class Controller: 
  
  def __init__(self, x, y): 
    """
        Initializes the controller
        args: 
          - x(int): width of screen 
            - y(int): height of screen  
        return: None 
        """ 
    pygame.init()
    pygame.event.pump() 
    self.screen = pygame.display.set_mode((x,y)) 
    pygame.display.set_caption("Play Piano!")
    self.state = "menu" 
    
    
  def mainloop(self): 
    """
        Includes procedures that need to continue throughout the entirety of the game 
        args: 
            - x (int): starting x coordinate 
            - y (int): starting y coordinate 
            - img_file (str): path to img file 
        """ 
    #select state loop
    running = True 
    while running: 
      #1. Event 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          running = False 
        elif self.state == "menu": 
          self.menuloop() 
        elif self.state == "game": 
          self.gameloop() 
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
    self.screen.fill((0, 0, 0),None) 
    pygame.draw.rect(self.screen, (202, 3, 252), (50, 50, 900, 450)) 
    song1 = Buttons(70, 70, 260, 110) 
    song2 = Buttons(370, 70, 260, 110)
    song3 = Buttons(670, 70, 260, 110)
    song4 = Buttons(70, 220, 260, 110)
    free_play = Buttons(370, 220, 260, 110) 
    song5 = Buttons(670, 220, 260, 110)
    song6 = Buttons(70, 370, 260, 110)
    song7 = Buttons(370, 370, 260, 110)
    song8 = Buttons(670, 370, 260, 110) 
    button_list = [song1, song2, song3, song4, free_play, song5, song6, song7, song8] 
    for i in button_list: 
      self.screen.blit(i.image, i.rect)
    pygame.display.flip() 
      
    while self.state == "menu": 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        #if event.type == pygame.MOUSEBUTTONDOWN:
          #if self.free_play.rect.collidepoint(event.pos) 
    
          
      
    self.state == "game" 
    self.mainloop() 
      #update data 

      #redraw 
      
  def gameloop(self): 
    """
    Manages game and includes the interactive piano keys and music notes 
      args: None 
      return: None 
    """ 
      #event loop 
    key_a = Keys(0) 
    key_s = Keys(125) 
    key_d = Keys(250) 
    key_f = Keys(375) 
    key_h = Keys(500) 
    key_j = Keys(625) 
    key_k = Keys(750) 
    key_l = Keys(875) 
    sharp_w = Keys(95, 300, 60, 150)
    sharp_e = Keys(220, 300, 60, 150)
    sharp_t = Keys(470, 300, 60, 150)
    sharp_u = Keys(595, 300, 60, 150)
    sharp_i = Keys(720, 300, 60, 150) 
    sharp_p = Keys(970, 300, 60, 150) 
    key_list = [key_a, key_s, key_d, key_f, key_h, key_j, key_k, key_l] 
    sharp_list = [sharp_w, sharp_e, sharp_t, sharp_u, sharp_i, sharp_p]
    for i in key_list: 
      pygame.draw.rect(self.screen, (255, 255, 255), i, 0) 
    for i in sharp_list: 
      pygame.draw.rect(self.screen, (0, 0, 0), i, 0) 
    pygame.display.flip() 
    for event in pygame.event.get(): 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_a: 
          print("a has been pressed") 
          
          

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
