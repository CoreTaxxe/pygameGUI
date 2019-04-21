import pygame
from fontobjects import render_text


class Label:
    def __init__(self,
                 POSITION,
                 TEXTSIZE,
                 TEXT="",
                 TEXTCOLOR=(0, 0, 0),
                 FONTSTYLE="freesansbold.ttf",
                 ):
        self.pos = POSITION
        self.size = TEXTSIZE
        self.text = TEXT
        self.textcolor = TEXTCOLOR
        self.fontstyle = FONTSTYLE

    def update(self, surface):
        render_text(self.text, self.pos, self.size, self.textcolor, self.fontstyle, "CENTER", surface)
