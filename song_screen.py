import pygame 
from button_object import StandardButton, PlayPauseButton, BackButton

class SongScreen (object):

    def __init__ (self, window, roster, callback_on_selected, text):
        
        self.GAME_FONT = pygame.font.SysFont("Bradley Hand", 20, bold = False, italic = False)

        self.run = True
        self.window = window
        self.roster = roster
        self.callback_on_selected = callback_on_selected
        self.text = text 
        self.run = True

        self.create_widgets()
        self.loop()

    def create_widgets(self):
        
        pygame.display.set_caption(self.text)
        self.window.fill((225, 227, 231))

        text_surface = self.GAME_FONT.render("Now Playing:", True, (0, 0, 0))
        self.window.blit(text_surface, (200, 19))

        White = pygame.image.load('225, 227, 231.png')
        White = pygame.transform.scale(White, (250, 250))
        image = White   
        self.window.blit(image, (200, 70))

        play_img = pygame.image.load('Play Button Icon.png')
        play_img = pygame.transform.scale(play_img, (50, 50))
        pause_img = pygame.image.load('Pause Button Icon.png')
        pause_img = pygame.transform.scale(pause_img, (50, 50))
        back_img = pygame.image.load('Back Button Icon.png')
        back_img = pygame.transform.scale(back_img, (50, 50))
        
        pause_button = StandardButton(175, 325, 50, 50, (225, 227, 231), "pause")
        unpause_button = StandardButton(275, 325, 50, 50, (225, 227, 231), "unpause")
        back_button = StandardButton(7, 340, 50, 50, (225, 227, 231), "back")

        pause_button = PlayPauseButton(pause_button)
        unpause_button = PlayPauseButton(unpause_button)
        back_button = BackButton(back_button)

        pause_button.standard_button.draw(window = self.window)
        unpause_button.standard_button.draw(window = self.window)
        back_button.standard_button.draw(window = self.window)

        for item in self.roster.song_buttons_list:

            item.standard_button.draw(window = self.window)
            item.standard_button.draw_line(window = self.window)
            item.add_text(window = self.window)
            self.window.blit(play_img, (275, 325))
            self.window.blit(pause_img, (175, 325))
            self.window.blit(back_img, (7, 340))
        
        self.roster.song_buttons_list.append(pause_button)
        self.roster.song_buttons_list.append(unpause_button)
        self.roster.song_buttons_list.append(back_button)
        
        pygame.display.update()

    def loop (self):
        
        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster.song_buttons_list:

                        if item.standard_button.click(mousepos[0], mousepos[1]):
                        
                            if len(item.standard_button.command) == 1:
                            
                                item.play(command = int(item.standard_button.command), roster = self.roster.song_buttons_list)
                                item.place_image(command = int(item.standard_button.command), roster = self.roster.song_buttons_list, window = self.window)
                            
                            elif item.standard_button.command == "pause":
                                item.pause()

                            elif item.standard_button.command == "unpause":
                                item.unpause()
                            
                            elif item.standard_button.command == "back":
                                
                                item.stop()
                                self.callback_on_selected()
                                self.run = False