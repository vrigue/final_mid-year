import pygame

from button_object import SongButtonRoster, GenreButtonRoster
from song_screen import SongScreen
from genre_screen import GenreScreen

class Jukebox_Manager (object):

    def __init__(self):
        
        self.window = pygame.display.set_mode((500, 400))
        self.roster = None
        self.run = True

    def setup_genre_screen(self):

        self.roster = GenreButtonRoster ("genre_list.txt")
        GenreScreen (window = self.window, roster = self.roster, callback_on_selected = self.setup_song_screen)

    def setup_song_screen(self, file_name, color_theme, text):
        
        self.roster = SongButtonRoster (file_name, color_theme)
        SongScreen (window = self.window, roster = self.roster, callback_on_selected = self.setup_genre_screen, text = text)
                              
def main():

    pygame.init()
    jukebox = Jukebox_Manager()
    jukebox.setup_genre_screen()

main()