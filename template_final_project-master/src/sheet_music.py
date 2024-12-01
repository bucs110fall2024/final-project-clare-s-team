import pygame 
import os 
class Sheet_music(pygame.sprite.Sprite):            #pygame.sprite.Sprite
    def __init__(self, file_name, x, y, w, h): 
        """ 
        description 
        """ 
        super().__init__() 
        self.file = file_name 
        self.image = pygame.Surface((w, h)) 
        self.rect = self.image.get_rect() 
        self.rect.x, self.rect.y = x, y 
        self.image.fill((255, 255, 255)) 
        self.pic = pygame.image.load(os.path.join("assets", self.file))
        self.image.blit(self.pic, self.rect) 