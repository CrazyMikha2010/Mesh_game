import pygame as pg
import random
from settings import *

pg.init()
pg.font.init()
pg.display.set_caption('Mezhibovskiy project')
clock = pg.time.Clock()
FPS = 60
w, h = 1080, 720
scr = pg.display.set_mode((w, h))

class Third_Fourth:
    def __init__(self):
        self.running = True
        self.rot = 0
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
    
    def third_fourth(self, rot):
        background = pg.image.load(mainpath + "/menu/34HillTower.png")
        scr.blit(background, (0, 0))

        wheel1 = pg.image.load(mainpath + "/menu/wheel1.png").convert_alpha()
        wheel1 = pg.transform.scale(wheel1, (75, 75))
        wheel1 = pg.transform.rotate(wheel1, rot)
        scr.blit(wheel1, (330, 470))
        wheel2 = pg.image.load(mainpath + "/menu/wheel2.png").convert_alpha()
        wheel2 = pg.transform.scale(wheel2, (75, 75))
        wheel2 = pg.transform.rotate(wheel2, rot)
        scr.blit(wheel2, (470, 370))

        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))

        font_m = pg.font.SysFont('Comic Sans MS', 30)

        text_third_fourth = 'Now that you’re finally standing next to her tower, you, as every other knight, have to make a brave act: field in front of tower is full of mines. From the top-left corner you can go down or right (using arrow keys). Your goal is to choose the path to the bottom-right corner such that the amount of mines you stepped on is the smallest. After crossing it, fortune will decide whether you’ll get to meet princess, or blow up as other contenders.'
        tmp_third_fourth = ['Now that you’re finally standing next to her tower, you, as every', ' other knight, have to make a brave act: field in front of', ' tower is full of mines. From the top-left corner you can go', ' down or right (using arrow keys). Your goal is to choose the', ' path to the bottom-right corner such that the amount of mines you', ' stepped on is the smallest. After crossing it, fortune will decide whether', ' you’ll get to meet princess, or blow up as other contenders.']

        for line in range(len(tmp_third_fourth)):
            backstory_scr = font_m.render(tmp_third_fourth[line], False, "white")
            scr.blit(backstory_scr, (10 if line > 0 else 40, 20 + 40 * line))

        next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
        next = pg.transform.scale(next, (200, 100))
        scr.blit(next, (440, 500))

        pg.display.flip()

    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if pg.Rect(440, 500, 200, 100).collidepoint(event.pos): # fourth level
                    if sound: self.click.play()
                    self.status = True

        self.third_fourth(self.rot)
        self.rot -= 10

        return self.running, self.status

if __name__ == "__main__":
    running = True
    tf = Third_Fourth()
    while running:
        running, status = tf.f(True)

