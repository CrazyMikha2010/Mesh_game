from settings import *

class First_Second:
    def __init__(self):
        self.running = True
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.grasshopper_x, self.grasshopper_y = 720, 540
        self.up = True

    def first_second(self):
        background = pg.image.load(mainpath + "/menu/Menu.png")
        scr.blit(background, (0, 0))

        grasshopper = pg.image.load(mainpath + "/images2/Grasshopper2.png").convert_alpha()
        grasshopper = pg.transform.scale(grasshopper, (130, 91))

        scr.blit(grasshopper, (self.grasshopper_x, self.grasshopper_y))
        self.grasshopper_y += 0.3 if self.up else -0.3
        if abs(540 - self.grasshopper_y) >= 5:
            self.up = not self.up
        self.grasshopper_x += 0.3 if not self.up else -0.3

        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))


        text_first_second = 'Good job, now that our friend is ready, he needs to cross the river that’s cutting his peaceful meadows from harsh outer world. He’ll cross it by jumping from lily to lily. He can either jump on the next one or the one after next. Also he needs to collect as much lilies for his princess as possible. Navigate the grasshopper so he would complete his mission. '
        lines_first_second = Text_Wrapper.text_wrapper(self, text_first_second, font_m, 1000)
        for i in range(len(lines_first_second)):
            backstory_scr = font_m.render(' '.join(lines_first_second[i]), False, "white")
            scr.blit(backstory_scr, (30 if i > 0 else 60, 20 + 40 * i))

        next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
        next = pg.transform.scale(next, (200, 100))
        scr.blit(next, (440, 500))

        pg.display.flip()

    def handle_mousePress(self, event_pos, sound):
        if pg.Rect(440, 500, 200, 100).collidepoint(event_pos): # second level
            if sound: self.click.play()
            self.status = True

    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mousePress(event.pos, sound)
        self.first_second()

        return self.running, self.status

if __name__ == "__main__":
    running = True
    fs = First_Second()
    while running:
        running, status = fs.f(True)

