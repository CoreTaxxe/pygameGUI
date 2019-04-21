import pygame
from fontobjects import render_text
import win32clipboard


class InputBox:
    def __init__(self,
                 POSITION,
                 SIZE,
                 COLOR,
                 TEXTCOLOR,
                 TEXT="",
                 TEXTSIZE=20,
                 FONTSTYLE="freesansbold.ttf",
                 ):
        self.pos = POSITION
        self.size = SIZE
        self.color = COLOR
        self.textcolor = TEXTCOLOR
        self.fontstyle = FONTSTYLE
        self.text = TEXT
        self.textsize = TEXTSIZE

        self.image = pygame.Surface([self.size[0], self.size[1]]).convert()
        self.image.fill(self.color)
        self.overdraw_image = pygame.Surface([self.size[0], self.size[1]]).convert()
        self.overdraw_image.fill(self.color)
        pygame.draw.rect(self.overdraw_image,
                         (int(self.color[0] / 2),
                          int(self.color[1] / 2),
                          int(self.color[2] / 2)),
                         (0, 0, self.size[0], self.size[1]), 3)

        self.rect = self.image.get_rect()
        self.active = False
        self.tick = False
        self.rect.center = self.pos
        self.tick_counter = 0

    def check_pressed(self, cursor):
        if self.rect.x < cursor[0] < self.rect.x + self.size[0] and \
                self.rect.y < cursor[1] < self.rect.y + self.size[1]:
            return True
        else:
            return False

    def handle_input(self, event):
        if event.unicode == "\x08":
            self.text = self.text[:-1]

        elif event.unicode == "\x16":
            self.text = self.text + self.get_clipboard()

        elif event.unicode == "\r":
            self.active = False

        else:
            self.text = self.text + event.unicode

    def update(self, surface):
        if self.tick_counter == 120:
            self.tick = True
            self.tick_counter = 0
        elif self.tick_counter > 100:
            self.tick = True
            self.tick_counter += 1
        else:
            self.tick_counter += 1
            self.tick = False

        surface.blit(self.image, self.rect)
        self.image.blit(self.overdraw_image, (0, 0))
        self.render()

    def render(self):
        if self.tick:
            render_text(self.text + "|", (10, 5), self.textsize, self.textcolor, self.fontstyle, "topleft", self.image)
        else:
            render_text(self.text, (10, 5), self.textsize, self.textcolor, self.fontstyle, "topleft", self.image)

    @staticmethod
    def get_clipboard():
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
