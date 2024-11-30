import pygame 
class Buttons(pygame.sprite.Sprite): 
    def __init__(self, x=0, y=0, width=100, height=100, text = "None", color = (120, 12, 250)): 
        """ 
        Initializes the Music object with the following attributes: 
        args: 
            - x (int): starting x coordinate 
            - y (int): starting y coordinate 
            - name (str): name of song 
        """ 
        super().__init__() 
        self.image = pygame.Surface((width, height)) 
        self.rect = self.image.get_rect() 
        self.rect.x, self.rect.y = x, y 
        self.color = color 
        self.text = text 
        self.image.fill(self.color) 
        text_color = (255, 255, 255) 
        self.message = pygame.font.SysFont(None, 36).render(self.text, True, text_color) 
        self.image.blit(self.message, (50,45)) 
    def glow(self): 
        """ 
        If note is next, it glows 
        args: None 
        return: None 
        """ 
        highlight_color = [] 
        for i, c in enumerate(self.color): 
            if c+50 < 255: 
                highlight_color.append(c+50) 
            else: 
                highlight_color.append(255) 
        self.image.fill(highlight_color) 
        self.image.blit(self.message, (0, 0)) 
    def default_color(self): 
        """ 
        Description 
        """ 
        self.image.fill(self.color) 
        self.image.blit(self.message, (0, 0)) 