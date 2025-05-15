from settings import *

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

        text_third_fourth = 'Now that you’re finally standing next to her tower, you, as every other knight, have to make a brave act: field in front of tower is full of mines. From the top;left corner you can go down or right. Your goal is to choose the path to the bottom;right corner such that the amount of mines you stepped on is the smallest. After crossing it, fortune will decide whether you’ll get to meet princess, or blow up as other contenders.'
        lines_third_fourth = Text_Wrapper.text_wrapper(self, text_third_fourth, font_m, 1000)
        for i in range(len(lines_third_fourth)):
            backstory_scr = font_m.render(' '.join(lines_third_fourth[i]), False, "white")
            scr.blit(backstory_scr, (30 if i > 0 else 60, 20 + 40 * i))

        next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
        next = pg.transform.scale(next, (200, 100))
        scr.blit(next, (440, 500))
        self.rot -= 10

        pg.display.flip()

    def handle_mosePress(self, event_pos, sound):
        if pg.Rect(440, 500, 200, 100).collidepoint(event_pos): # fourth level
            if sound: self.click.play()
            self.status = True

    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mosePress(event.pos, sound)

        self.third_fourth(self.rot)

        return self.running, self.status

if __name__ == "__main__":
    running = True
    tf = Third_Fourth()
    while running:
        running, status = tf.f(True)

