import pygame
from pygame import mixer
from pygame.locals import *
pygame.init()

class StandardButton (object):

    def __init__(self, x, y, width, height, color, index): 

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = index

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word) 

    def click(self, mousex, mousey):

        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
            
        return False

    def draw_line(self, window):

        black = (0, 0, 0)
        white = (255, 255, 255)

        pygame.draw.line(window, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(window, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

class SongButton (object):

    def __init__(self, button, music, image, txt):

        self.standard_button = button
        self.music = music
        self.image = image
        self.txt = txt
        self.text_color = (255, 255, 255)

    def play(self, command, roster):

        pygame.mixer.init()
        mixer.music.load(str(roster[command].music))
        mixer.music.set_volume(0.7)
        mixer.music.play()
    
    def place_image(self, command, roster, window):

        image = pygame.image.load(str(roster[command].image))
        image = pygame.transform.scale(image, (250,250))
        window.blit(image, (200, 51))
        pygame.display.update()

    def add_text(self, window):

        font = pygame.font.SysFont('Bradley Hand', 30)
        down = 0

        if len(self.txt) > 0 and len(self.txt) <= 9:
            font = pygame.font.SysFont("Bradley Hand", 21)
            down = 13
        elif len(self.txt) > 9 and len(self.txt) <= 11:
            font = pygame.font.SysFont("Bradley Hand", 17)
            down = 15
        elif len(self.txt) > 11:
            font = pygame.font.SysFont("Bradley Hand", 15)
            down = 16

        text_img = font.render(self.txt, True, self.text_color)
        text_len = text_img.get_width()
        window.blit(text_img, (self.standard_button.x + int(self.standard_button.width / 2) - int(text_len / 2), self.standard_button.y + down))

class PlayPauseButton (object):

    def __init__(self, button):

        self.standard_button = button 

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

class GenreButton (object):

    def __init__(self, button, file_name, color_theme, txt, caption_txt):

        self.standard_button = button 
        self.file_name = file_name
        self.color_theme = color_theme
        self.txt = txt 
        self.caption_txt = caption_txt
        self.text_color = (255, 255, 255)

    def add_text(self, window):

        font = pygame.font.SysFont('Bradley Hand', 30)
        down = 0

        if len(self.txt) > 0 and len(self.txt) < 7:
            font = pygame.font.SysFont("Bradley Hand", 25)
            down = 32
        elif len(self.txt) == 7:
            font = pygame.font.SysFont("Bradley Hand", 27)
            down = 32
        elif len(self.txt) > 7:
            font = pygame.font.SysFont("Bradley Hand", 20)
            down = 37

        text_img = font.render(self.txt, True, self.text_color)
        text_len = text_img.get_width()
        window.blit(text_img, (self.standard_button.x + int(self.standard_button.width / 2) - int(text_len / 2), self.standard_button.y + down))
    
class BackButton (object):

    def __init__(self, button):

        self.standard_button = button 

    def stop (self):
        pygame.mixer.music.stop()

class SongButtonRoster (object):


    def __init__(self, file_name, color_theme):

        self.song_buttons_list = []
        y = 25
        c = 0
        index = 0 
        f = open(file_name)

        t = color_theme[0]
        u = color_theme[1]
        z = color_theme[2]

        for line in f:
            c += 1

            # say if button added or +1 in button counter, change the color
            # make each number (x, u, z) a variable that will then change or get subtracted

            if c + 1:
                
                if z < u and u > 100:
                    u -= 10
                    z += 25

                elif z < u:
                    u += 15
                    z += 15

                elif u < z:
                    t += 5
                    u += 40

                newButtonColor = (int(t), int(u), int(z))

            line = line.strip()
            line_elements = line.split(';')
            b = StandardButton(50, y, 100, 50, newButtonColor, str(index))
            b = SongButton(button = b, music = line_elements[1], image = line_elements[2], txt = line_elements[0])
            self.song_buttons_list.append(b)

            y += 75 
            index += 1

class GenreButtonRoster (object):

    def __init__(self, file_name):

        self.genre_buttons_list = []
        x = 20
        c = 0
        index = 0 
        f = open(file_name)

        t = 0
        u = 179
        z = 255


        for line in f:
            c += 1

            # say if button added or +1 in button counter, change the color
            # make each number (x, u, z) a variable that will then change or get subtracted

            if c + 1:
                t += 24
                u += 12
        
                newButtonColor = (int(t), int(u), int(z))

            line = line.strip()
            line_elements = line.split(';')
            color_theme = (int(line_elements[3]), int(line_elements[4]), int(line_elements[5]))

           # self, button, file_name, color_theme, txt, caption_txt
            b = StandardButton(x, 275, 100, 100, newButtonColor, str(index))
            b = GenreButton(b, line_elements[2], color_theme = color_theme, txt = line_elements[0], caption_txt = line_elements[1])

            self.genre_buttons_list.append(b)

            x += 120
            index += 1