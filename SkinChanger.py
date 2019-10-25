import pygame as pg

pg.init()

Red = (221, 0, 0)
Green = (0, 187, 0)
Yellow = (254, 246, 0)
Blue = (0, 155, 254)
Violet = (48, 0, 155)
Orange = (254, 98, 98)

def colourSwap(surf, from_, to_):
    arr = pg.PixelArray(surf)
    arr.replace(from_, to_)
    del arr

class image:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.image.load('rainbow.png').convert()
        self.rect = self.image.get_rect(center=self.screen_rect)
        colourSwap(self.image, (0, 187, 0))

    def draw(self, surf):
        surf.blit(self.image, self.rect)

screen = pg.dispaly.set_mode((800, 600))
screen_rect = screen.get_rect()
player = image(screen_rect)
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.draw(screen)
        pg.display.update()