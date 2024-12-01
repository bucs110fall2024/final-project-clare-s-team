import pygame 
import pygame.freetype 
from src.buttons import Buttons 
from src.arrow import Arrow 
from src.sheet_music import Sheet_music
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
    self.state = "start" 
    
    
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
        elif self.state == "start": 
          self.startloop() 
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
  def startloop(self): 
    """ 
    description 
    """ 
    self.screen.fill((0, 0, 0),None) 
    pygame.draw.rect(self.screen, (202, 3, 252), (50, 50, 900, 450)) 
    self.welcome = Buttons(250, 70, 500, 95, "Welcome to Play Piano!", center = (14, 40), fsize = 60) 
    self.play = Buttons(325, 325, 75, 60, "Play", center = (10, 20)) 
    self.chart = Buttons(530, 325, 135, 60, "Key Chart", center = (10, 20)) 
    self.screen.blit(self.welcome.image, self.welcome.rect) 
    self.screen.blit(self.play.image, self.play.rect) 
    self.screen.blit(self.chart.image, self.chart.rect) 
    pygame.display.flip() 
    while self.state == "start": 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
          if self.play.rect.collidepoint(event.pos): 
            self.state = "menu" 
            self.menuloop()
          elif self.chart.rect.collidepoint(event.pos): 
            self.state = "chart" 
            self.chartloop() 
  def chartloop(self): 
    """ 
    description 
    """ 
    self.screen.fill((0, 0, 0))
    self.keychart = Sheet_music("keychart.jpg", 100, 100, 500, 300) 
    self.screen.blit(self.keychart.image, self.keychart.rect) 
    self.menu_button = Buttons(910, 20, 75, 35, "Menu", (202, 3, 252), (0, 0, 0), (5, 5)) 
    self.screen.blit(self.menu_button.image, self.menu_button.rect) 
    pygame.display.flip() 
    while self.state == "chart": 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
          if self.menu_button.rect.collidepoint(event.pos): 
            self.state = "menu" 
      
      
        
  def menuloop(self): 
    """
    Manages menu screen and its interactive buttons 
      args: None 
      return: None 
    """ 
      #event loop 
    self.screen.fill((0, 0, 0),None) 
    pygame.draw.rect(self.screen, (202, 3, 252), (50, 50, 900, 450)) 
    self.song1 = Buttons(70, 70, 260, 110, "C Major Scale") 
    self.song2 = Buttons(370, 70, 260, 110, "Happy Birthday", center = (42, 45)) 
    self.song3 = Buttons(670, 70, 260, 110, "Ba Ba Black Sheep", center = (17, 45)) 
    self.song4 = Buttons(70, 220, 260, 110, "Hot Cross Buns", center = (33, 45)) 
    self.free_play = Buttons(370, 220, 260, 110, "Free Play", center = (70, 45)) 
    self.song5 = Buttons(670, 220, 260, 110, "Jack Be Nimble") 
    self.song6 = Buttons(70, 370, 260, 110, "Wheels On the Bus", center = (12, 45)) 
    self.song7 = Buttons(370, 370, 260, 110, "London Bridge") 
    self.song8 = Buttons(670, 370, 260, 110, "Hole in Your Bucket", center = (12, 45)) 
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
            self.song = "free_play" 
            self.state = "game"
          elif self.song1.rect.collidepoint(event.pos): 
            self.song = "1" 
            self.state = "game"
          elif self.song2.rect.collidepoint(event.pos): 
            self.song = "2" 
            self.state = "game" 
          elif self.song3.rect.collidepoint(event.pos): 
            self.song = "3" 
            self.state = "game" 
          elif self.song4.rect.collidepoint(event.pos): 
            self.song = "4" 
            self.state = "game" 
          elif self.song5.rect.collidepoint(event.pos): 
            self.song = "5" 
            self.state = "game" 
          elif self.song6.rect.collidepoint(event.pos): 
            self.song = "6" 
            self.state = "game" 
          elif self.song7.rect.collidepoint(event.pos): 
            self.song = "7" 
            self.state = "game" 
          elif self.song8.rect.collidepoint(event.pos): 
            self.song = "8" 
            self.state = "game" 
      pygame.display.flip() 
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
    self.menu_button = Buttons(910, 20, 75, 35, "Menu", (202, 3, 252), (0, 0, 0), (5, 5)) 
    self.screen.blit(self.menu_button.image, self.menu_button.rect) 
    self.key_a = Buttons(0, 300, 120, 250, "C", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_s = Buttons(125, 300, 120, 250, "D", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_d = Buttons(250, 300, 120, 250, "E", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_f = Buttons(375, 300, 120, 250, "F", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_h = Buttons(500, 300, 120, 250, "G", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_j = Buttons(625, 300, 120, 250, "A", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_k = Buttons(750, 300, 120, 250, "B", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.key_l = Buttons(875, 300, 120, 250, "C", (255, 255, 255), (0, 0, 0), (50, 195)) 
    self.sharp_w = Buttons(95, 300, 60, 150,"C#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    self.sharp_e = Buttons(220, 300, 60, 150,"D#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    self.sharp_t = Buttons(470, 300, 60, 150,"F#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    self.sharp_u = Buttons(595, 300, 60, 150,"G#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    self.sharp_i = Buttons(720, 300, 60, 150,"A#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    self.sharp_p = Buttons(970, 300, 60, 150,"C#", (0, 0, 0), (255, 255, 255), (15, 100)) 
    key_list = [self.key_a, self.key_s, self.key_d, self.key_f, self.key_h, self.key_j, self.key_k, self.key_l] 
    sharp_list = [self.sharp_w, self.sharp_e, self.sharp_t, self.sharp_u, self.sharp_i, self.sharp_p] 
    for i in key_list: 
      self.screen.blit(i.image, i.rect) 
    for i in sharp_list: 
      self.screen.blit(i.image, i.rect) 
    if self.song == "1": 
      self.image = Sheet_music("CMajor_scale.jpg", 70, 15, 700, 200) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "2": 
      self.image = Sheet_music("happy_bday.png", 60, 10, 650, 280) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "3": 
      self.image = Sheet_music("baa_sheep.jpg", 75, 15, 700, 240) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "4": 
      self.image = Sheet_music("Hot_Cross_Buns.jpg", 70, 15, 700, 220) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "5": 
      self.image = Sheet_music("jack_nimble.jpg", 70, 15, 700, 210) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "6": 
      self.image = Sheet_music("wheels_on_bus.jpg", 70, 15, 700, 220) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "7": 
      self.image = Sheet_music("london_bridge.jpg", 70, 15, 700, 220) 
      self.screen.blit(self.image.image, self.image.rect) 
    elif self.song == "8": 
      self.image = Sheet_music("hole_in_bucket.jpg", 70, 15, 700, 220) 
      self.screen.blit(self.image.image, self.image.rect) 
    pygame.display.flip() 
    while self.state == "game": 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          self.state == "None" 
          pygame.quit() 
          exit() 
        if event.type == pygame.MOUSEBUTTONDOWN: 
          if self.menu_button.rect.collidepoint(event.pos): 
            self.state = "menu" 
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
            # self.key_l.glow() 
            # self.screen.blit(self.key_l.image, self.key_l.rect) 
          elif event.key == pygame.K_w: 
            self.sharp_w.key_down("C#.ogg") 
          elif event.key == pygame.K_e: 
            self.sharp_e.key_down("D#.ogg") 
          elif event.key == pygame.K_t: 
            self.sharp_t.key_down("F#.ogg") 
          elif event.key == pygame.K_u: 
            self.sharp_u.key_down("G#.ogg") 
          elif event.key == pygame.K_i: 
            self.sharp_i.key_down("A#.ogg") 
          pygame.display.flip() 
      # else: 

      #update data 

      #redraw 
