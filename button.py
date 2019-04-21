import pygame
import os
from fontobjects import render_text


class Button:
    def __init__(self,
                 POSITION,
                 SIZE,
                 TEXT="",
                 IMAGE=None,
                 IMAGEPATH="",
                 ALIGN="CENTER",
                 COLOR=(255, 255, 255),
                 TRANSPARENCY=100,
                 TEXTCOLOR=(0, 0, 0),
                 TEXTPOS=(0, 0),
                 TEXTALIGN="CENTER",
                 TEXTSIZE=20,
                 FONTSTYLE="freesansbold.ttf"):
        self.pos = POSITION
        self.size = SIZE
        self.align = ALIGN
        self.text = TEXT
        self.color = COLOR
        self.textcolor = TEXTCOLOR
        self.textpos = TEXTPOS
        self.textalign = TEXTALIGN
        self.textsize = TEXTSIZE
        self.fontstyle = FONTSTYLE
        self.path = IMAGEPATH
        self.transparency = TRANSPARENCY
        self.hovered = False

        if IMAGE is not None:
            self.image = pygame.image.load(os.path.join(self.path, IMAGE))
            self.image.convert()
        else:
            self.image = pygame.Surface([self.size[0], self.size[1]], pygame.SRCALPHA).convert()
            self.color = (self.color[0], self.color[1], self.color[2], (int(255 / 100 * TRANSPARENCY)))
            self.image.fill(self.color)

        self.rect = self.image.get_rect()
        if self.align == "CENTER":
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos

        render_text(self.text, self.textpos, self.textsize, self.textcolor, self.fontstyle, self.textalign, self.image)

    def update(self, surface):
        surface.blit(self.image, self.rect)
        if self.hovered:
            pygame.draw.rect(surface, (200, 50, 50), self.rect, 2)

    def check_pressed(self, cursor):
        if self.rect.x < cursor[0] < self.rect.x + self.size[0] and \
                self.rect.y < cursor[1] < self.rect.y + self.size[1]:
            return True
        else:
            return False

    def check_hover(self, cursor):
        if self.rect.x < cursor[0] < self.rect.x + self.size[0] and \
                self.rect.y < cursor[1] < self.rect.y + self.size[1]:
            self.hovered = True
            return True
        else:
            self.hovered = False
