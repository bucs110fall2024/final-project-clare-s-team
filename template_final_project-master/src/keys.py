import pygame 
class Keys: 
    def __init__(self, x, y=300, width=120, height=250): 
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
        
    def play_note(self): 
        """
        Plays note of key 
        args:None 
        return: None 
        """
        pass
    def press_down(self): 
        """ 
        Changes color of key pressed a shade darker 
        args: None 
        return: None 
        """ 
        pass