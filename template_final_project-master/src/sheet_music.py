import pygame 
import os 
class Sheet_music(pygame.sprite.Sprite): 
    def __init__(self, file_name, x, y, w, h): 
        """ 
        Initializes the Sheet_music class which creates a surface with an image from the "assets" folder. 
        args: 
            - file_name(str): name of the image file 
            - x(int): x coordinate of the top left corner of the object 
            - y(int): y coordinate of the top left corner of the object 
            - w(int): width of the object 
            - h(int): height of the object 
        return: None 
        """ 
        super().__init__() 
        self.file = file_name 
        self.image = pygame.Surface((w, h)) 
        self.rect = self.image.get_rect() 
        self.rect.x, self.rect.y = x, y 
        self.image.fill((0, 0, 0)) 
        self.pic = pygame.image.load(os.path.join("assets", self.file))
        self.image.blit(self.pic, self.rect) 