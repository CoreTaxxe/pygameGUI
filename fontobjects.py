import pygame


def create_text_object(text, font, color):
    textsurface = font.render(str(text), True, color)
    return textsurface, textsurface.get_rect()


def render_text(text, position, textsize, textcolor, fontstyle, textalign, surface):
    textlabel = pygame.font.Font(str(fontstyle), textsize)
    textsurface, textsurfacerect = create_text_object(text, textlabel, textcolor)
    if textalign == "CENTER":
        textsurfacerect.center = int(surface.get_rect().size[0] / 2), int(surface.get_rect().size[1] / 2)
    else:
        textsurfacerect.topleft = position

    surface.blit(textsurface, textsurfacerect)


def render_text_as_label(text, position, textsize, textcolor, fontstyle, textalign, surface):
    textlabel = pygame.font.Font(str(fontstyle), textsize)
    textsurface, textsurfacerect = create_text_object(text, textlabel, textcolor)
    if textalign == "CENTER":
        textsurfacerect.center = position
    else:
        textsurfacerect.topleft = position

    surface.blit(textsurface, textsurfacerect)
