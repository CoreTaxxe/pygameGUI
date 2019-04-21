import pygame
import sys

from button import Button
from label import Label
from inputbox import InputBox

pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

# the hand cursor
_HAND_CURSOR = (
    "     XX         ",
    "    X..X        ",
    "    X..X        ",
    "    X..X        ",
    "    X..XXXXX    ",
    "    X..X..X.XX  ",
    " XX X..X..X.X.X ",
    "X..XX.........X ",
    "X...X.........X ",
    " X.....X.X.X..X ",
    "  X....X.X.X..X ",
    "  X....X.X.X.X  ",
    "   X...X.X.X.X  ",
    "    X.......X   ",
    "     X....X.X   ",
    "     XXXXX XX   ")

_HCURS, _HMASK = pygame.cursors.compile(_HAND_CURSOR, ".", "X")
HAND_CURSOR = ((16, 16), (5, 1), _HCURS, _HMASK)
# pygame.mouse.set_cursor(*HAND_CURSOR)
default = pygame.mouse.get_cursor()
##########################################################ignore abouve####################


example_Button = Button(POSITION=(250, 100), SIZE=(100, 100), TEXT="Button")  # there are more default changeable params
example_Label = Label(POSITION=(250, 200), TEXTSIZE=20, TEXT="I am a Label")  # there are more params
example_Input = InputBox(POSITION=(250, 400), SIZE=(100, 30), COLOR=(100, 100, 255), TEXTCOLOR=(255, 255, 255))

pygame.key.set_repeat(50,100)
while True:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if example_Input.active:
                example_Input.handle_input(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if example_Button.check_pressed(mouse_pos):
                print("You pressed a Button ")

            if example_Input.check_pressed(mouse_pos):
                example_Input.active = True
            else:
                example_Input.active = False

        if event.type == pygame.MOUSEMOTION:
            if example_Button.check_hover(mouse_pos):
                pygame.mouse.set_cursor(*HAND_CURSOR)
            else:
                pygame.mouse.set_cursor(*default)

    screen.fill((200, 200, 200))

    """update funcion below"""
    example_Button.update(screen)
    example_Label.update(screen)
    example_Input.update(screen)

    pygame.display.flip()
    clock.tick(60)
