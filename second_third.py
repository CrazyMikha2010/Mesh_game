from settings import *

class Second_Third:
    def __init__(self):
        self.running = True
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.grasshopper_x, self.grasshopper_y = 720, 540
        self.up = True

    def second_third(self):
        background = pg.image.load(mainpath + "/images3/3Table_structure.png")
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


        text_second_third = 'Yay! Now he has got a gift for his loved one. All that’s left is to get over the hill. Before last hike grasshopper decided to stop at tavern. The owner there loves gambling, and he suggested a game: he’ll put 10 numbers in any order he wants, and your goal is to highlight the longest increasing subsequence. If your subsequence will be shorter that his, than you have to buy another drink, otherwise he’ll do you a favour and drive you across the hill. '
        lines_second_third = Text_Wrapper.text_wrapper(self, text_second_third, font_m, 1000)
        for i in range(len(lines_second_third)):
            backstory_scr = font_m.render(' '.join(lines_second_third[i]), False, "white")
            scr.blit(backstory_scr, (30 if i > 0 else 60, 20 + 40 * i))

        next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
        next = pg.transform.scale(next, (200, 100))
        scr.blit(next, (440, 500))

        pg.display.flip()

    def handle_mousePress(self, event_pos, sound):
        if pg.Rect(440, 500, 200, 100).collidepoint(event_pos): # third level
            if sound: self.click.play()
            self.status = True

    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mousePress(event.pos, sound)
                
        self.second_third()
        return self.running, self.status

if __name__ == "__main__":
    running = True
    st = Second_Third()
    while running:
        running, status = st.f(True)

