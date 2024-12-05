import pygame 
import os 
#Modeled after ch08/examples/button_model.py 
class Buttons(pygame.sprite.Sprite): 
    def __init__(self, x=0, y=0, width=100, height=100, text = "None", color = (120, 12, 250), text_color = (255, 255, 255), center = (50, 45), fontsize = 36): 
        """ 
        Initializes the Buttons class which generates a surface with a box and text on it 
        args: 
            - x(int): x coordinate of the top left corner of box object 
            - y(int): y coordinate of the top left corner of box object 
            - width(int): width of the box 
            - height(int): height of the box 
            - text(str): desired message to display on the box 
            - color(int): tuple of integers with RGB value of the box 
            - text_color(int): tuple of integers with RGB value of the text
            - center(int): tuple of integers with location of the text within the box 
            - fontsize(int): size of the text's font 
        return: None 
        """ 
        super().__init__() 
        self.image = pygame.Surface((width, height)) 
        self.rect = self.image.get_rect() 
        self.rect.x, self.rect.y = x, y 
        self.color = color 
        self.text = text 
        self.text_color = text_color 
        self.center = center 
        self.image.fill(self.color) 
        self.message = pygame.font.SysFont(None, fontsize).render(self.text, True, text_color) 
        self.image.blit(self.message, center) 
    def key_down(self, file_name): 
        """ 
        Loads the corresponding sound file of the key pressed and plays the note 
        args: 
            - file_name(str): name of a sound file 
        return: None 
        """ 
        self.sound = file_name 
        note = pygame.mixer.Sound(os.path.join("assets/music_notes", self.sound)) 
        pygame.mixer.Sound.play(note) 
    def glow(self): 
        """ 
        Changes the shade of the object by 50. If the object is black, it gets lighter. 
        If it's white or any other color, it gets darker. 
        args: None 
        return: None 
        """ 
        highlight_color = [] 
        for i, c in enumerate(self.text_color): 
            if c == 255: 
                highlight_color.append(255-50) 
            elif c == 0: 
                highlight_color.append(50) 
            elif c+50 < 255: 
                highlight_color.append(c+50) 
            else: 
                highlight_color.append(255) 
        self.image.fill(highlight_color) 
        self.image.blit(self.message, self.center) 
    def default_color(self): 
        """ 
        Fills the object with the original inputted color and 
        reprints the message onto the object. 
        args: None 
        return: None 
        """ 
        self.image.fill(self.color) 
        self.image.blit(self.message, self.center) 
    