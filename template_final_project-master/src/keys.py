import pygame 
import os 
class Keys: 
    def __init__(self, x, y=300, width=120, height=250, color=(255, 255, 255)): 
        """ 
        Initializes the key object 
        args: 
            - x (int): starting x coordinate 
            - y (int): starting y coordinate 
            - width(int): width of key 
            - height(int): height of key 
        """ 
        self.rect = pygame.Rect(x, y, width, height) 
        self.rect.x = x 
        self.rect.y = y 
        self.rect.width = width 
        self.rect.height = height 
        self.color = color 
        
    def play_note(self): 
        """ 
        Plays note of key 
        args:None 
        return: None 
        """ 
        pass 
    def key_down(self, sound): 
        """ 
        Changes color of key pressed a shade darker 
        args: None 
        return: None 
        """ 
        self.sound = sound 
        note = pygame.mixer.Sound(os.path.join("assets/Music - unknown album", self.sound)) 
        pygame.mixer.Sound.play(note) 
        pygame.time.wait(1000)
        pygame.mixer.music.stop()
        self.darker = (205, 205, 205) 
        