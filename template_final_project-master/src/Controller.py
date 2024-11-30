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
    self.song1 = Buttons(70, 70, 260, 110, "Song #1") 
    self.song2 = Buttons(370, 70, 260, 110, "Song #2") 
    self.song3 = Buttons(670, 70, 260, 110, "Song #3") 
    self.song4 = Buttons(70, 220, 260, 110, "Song #4") 
    self.free_play = Buttons(370, 220, 260, 110, "Free Play") 
    self.song5 = Buttons(670, 220, 260, 110, "Song #5") 
    self.song6 = Buttons(70, 370, 260, 110, "Song #6") 
    self.song7 = Buttons(370, 370, 260, 110, "Song #7") 
    self.song8 = Buttons(670, 370, 260, 110, "Song #8") 
    button_list = [self.song1, self.song2, self.song3, self.song4, self.free_play, self.song5, self.song6, self.song7, self.song8] 
    for i in button_list: 
      self.screen.blit(i.image, i.rect) 
    pygame.display.flip() 
      
    while self.state == "menu": 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        # if event.type == pygame.MOUSEMOTION: 
        #   if self.song1.rect.collidepoint(event.pos): 
        #     self.song1.glow() 
        #   else: 
        #     self.song1.default_color()  
        elif event.type == pygame.MOUSEBUTTONDOWN: 
          if self.free_play.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "None" 
          elif self.song1.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "1" 
          elif self.song2.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "2" 
          elif self.song3.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "3" 
          elif self.song4.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "4" 
          elif self.song5.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "5" 
          elif self.song6.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "6" 
          elif self.song7.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "7" 
          elif self.song8.rect.collidepoint(event.pos): 
            self.gameloop() 
            self.song = "8" 
          
            
      pygame.display.flip() 
    
          
      
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
    self.screen.fill((0, 0, 0), None) 
    self.key_a = Keys(0) 
    self.key_s = Keys(125) 
    self.key_d = Keys(250) 
    self.key_f = Keys(375) 
    self.key_h = Keys(500) 
    self.key_j = Keys(625) 
    self.key_k = Keys(750) 
    self.key_l = Keys(875) 
    self.sharp_w = Keys(95, 300, 60, 150, (0, 0, 0)) 
    self.sharp_e = Keys(220, 300, 60, 150, (0, 0, 0)) 
    self.sharp_t = Keys(470, 300, 60, 150, (0, 0, 0)) 
    self.sharp_u = Keys(595, 300, 60, 150, (0, 0, 0)) 
    self.sharp_i = Keys(720, 300, 60, 150, (0, 0, 0)) 
    self.sharp_p = Keys(970, 300, 60, 150, (0, 0, 0)) 
    key_list = [self.key_a, self.key_s, self.key_d, self.key_f, self.key_h, self.key_j, self.key_k, self.key_l] 
    sharp_list = [self.sharp_w, self.sharp_e, self.sharp_t, self.sharp_u, self.sharp_i, self.sharp_p] 
    for i in key_list: 
      pygame.draw.rect(self.screen, i.color, i, 0) 
    for i in sharp_list: 
      pygame.draw.rect(self.screen, i.color, i, 0) 
    pygame.display.flip() 
    while True:       #self.state == "game"
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        if event.type == pygame.KEYDOWN: 
          if event.key == pygame.K_a: 
            self.key_a.key_down("do-c.ogg") 
          elif event.key == pygame.K_s: 
            self.key_s.key_down("re-d.ogg") 
          elif event.key == pygame.K_d: 
            self.key_d.key_down("mi-e.ogg") 
          elif event.key == pygame.K_f: 
            self.key_f.key_down("fa-f.ogg") 
          elif event.key == pygame.K_h: 
            self.key_h.key_down("so-g.ogg") 
          elif event.key == pygame.K_j: 
            self.key_j.key_down("la-a.ogg") 
          elif event.key == pygame.K_k: 
            self.key_k.key_down("ti-b.ogg") 
          elif event.key == pygame.K_l: 
            self.key_l.key_down("octave-do-c.ogg") 
      #     pygame.draw.rect(self.screen, self.key_a.darker, self.key_a) 
      #     pygame.display.flip() 
      # else: 
        
          
          
          

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
