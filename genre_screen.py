import pygame
from button_object import StandardButton

class GenreScreen (object):

    def __init__(self, window, roster, callback_on_selected):

        self.GAME_FONT = pygame.font.SysFont("Bradley Hand", 24, bold = False, italic = False)

        self.window = window
        self.callback_on_selected = callback_on_selected
        self.roster = roster 
        self.run = True

        self.create_widgets()
        self.loop()

    def create_widgets(self):

        pygame.display.set_caption('Welcome to the Jukebox!')
        self.window.fill((225, 227, 231))
        
        text_surface = self.GAME_FONT.render("Playlists:", True, (0, 0, 0))
        self.window.blit(text_surface, (205, 232))

        title_img = pygame.image.load('titleimage.png')
        title_img = pygame.transform.scale(title_img, (310, 230))

        for item in self.roster.genre_buttons_list:

            item.standard_button.draw(window = self.window)
            item.standard_button.draw_line(window = self.window)
            item.add_text(window = self.window)
            self.window.blit(title_img, (93.5, 3))
        
        pygame.display.update()
        
    def loop (self):
        
        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster.genre_buttons_list:
                        
                        if item.standard_button.click(mousepos[0], mousepos[1]):
                        
                            self.callback_on_selected(item.file_name, item.color_theme, item.caption_txt)
                            self.run = False