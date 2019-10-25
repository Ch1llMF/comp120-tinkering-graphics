import pygame as pg

pg.init()

COLORKEY = (0, 0, 0)  # black

# RGB Values for each colour
RED = (221, 0, 0)
ORANGE = (254, 98, 98)
YELLOW = (254, 246, 0)
GREEN = (0, 187, 0)
BLUE = (0, 155, 254)
INDIGO = (0, 0, 131)
VIOLET = (48, 0, 155)


def swap_color(surf, from_, to_):
    arr = pg.PixelArray(surf)
    arr.replace(from_, to_) # change these in order to select colours
    del arr


class Rainbow:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.image.load('rainbow.png').convert()
        self.rect = self.image.get_rect(center=self.screen_rect.center)
        swap_color(self.image, (0, 187, 0), COLORKEY)
        self.image.set_colorkey(COLORKEY)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

# This creates the pop up screen
screen = pg.display.set_mode((1920, 1080))
screen_rect = screen.get_rect()
player = Rainbow(screen_rect)
done = False
while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    player.draw(screen)
    pg.display.update()