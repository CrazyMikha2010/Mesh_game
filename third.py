from settings import *

class Third:
    def __init__(self):
        self.running = True
        self.color = [False] * 10
        self.end = False
        self.nums = [random.randint(-9, 99) for _ in range(10)]
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.click2 = pg.mixer.Sound(mainpath + "/sound/click2.wav")
        

    def LIS(self):
        n = len(self.nums)
        help = [0] * n
        for i in range(n):
            cur_num = self.nums[i]
            max_len = 0
            for j in range(i - 1, -1, -1):
                tmp_num = self.nums[j]
                cur_len = help[j]
                if cur_num > tmp_num and max_len < cur_len:
                    max_len = cur_len
            help[i] = max_len + 1
        return max(help)

    def draw_grid(self, color, hover, cursor_pos):
        table_structure = pg.image.load(mainpath + "/images3/3Table_structure.png")
        leg = pg.image.load(mainpath + "/images3/3Leg.png")

        scr.blit(table_structure, (0, 0))
        pg.draw.rect(scr, (219, 177, 138), (40, 310, 1000, 100))
        for i in range(len(self.nums)):
            if color[i]: pg.draw.rect(scr, "light green", (i * 100 + 40, 310, 105, 100))
            pg.draw.rect(scr, "black", (i * 100 + 40, 310, 105, 100), 5)
            value = font_xl.render(f'{self.nums[i]}', False, "black")
            coords = (i * 100 + 55, 307) if len(str(self.nums[i])) == 2 else (i * 100 + 70, 307)
            scr.blit(value, coords)


        x = 20 if hover else 0
        background_color = (219 - x, 177 - x, 138 - x)
        font_color = (0, 0, 0)
        
        submit = font_l.render('submit', False, font_color)
        pg.draw.rect(scr, background_color, (900, 5, 150, 70), border_radius=10)
        scr.blit(submit, (910, 10))

        scr.blit(leg, (cursor_pos[0] - 560, cursor_pos[1] - 30))
        subseq = []
        for i in range(10):
            if self.color[i]:
                subseq.append(self.nums[i])
        if sorted(subseq) != subseq and len(subseq) > 0:
            warning = font_m.render('Your subsequence is not increasing', False, (255, 0, 0))
            scr.blit(warning, (200, 0))
        pg.display.flip()

        return self.nums
    
    def end_scr(self, scr, res):
        lis = self.LIS()
        if lis == res:
            victory = True
        else: 
            victory = False
        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))

        if victory:
            good_boy = pg.image.load(mainpath + "/images3/3Goodboy.png").convert_alpha()
            next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
            next = pg.transform.scale(next, (200, 100))
            scr.blit(good_boy, (0, 0))
            scr.blit(next, (440, 500))
        else:
            bad_boy = pg.image.load(mainpath + "/images3/3Badboy.png").convert_alpha()
            again = pg.image.load(mainpath + "/images/Again-transp-2.png").convert_alpha()
            again = pg.transform.scale(again, (200, 100))
            scr.blit(bad_boy, (0, 0))
            scr.blit(again, (440, 500))

        pg.display.flip()

        return victory
    
    def f(self, sound):
        if not self.end: pg.mouse.set_visible(False) # Hide cursor here
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if not self.end:
                        x, y = pg.mouse.get_pos()
                        if 310 <= y <= 410 and 40 <= x <= 1040:
                            if sound: self.click2.play()
                            self.color[(x - 40) // 100] = not self.color[(x - 40) // 100]

                        elif pg.Rect((900, 10, 150, 70)).collidepoint(pg.mouse.get_pos()): # submit button press
                            pg.mouse.set_visible(True) # Reveal cursor here
                            if sound: self.click.play()
                            subseq = []
                            for i in range(10):
                                if self.color[i]:
                                    subseq.append(self.nums[i])
                            if sorted(subseq) == subseq and len(subseq) > 0:
                                self.end = True
                                self.victory = self.end_scr(scr, len(subseq))
                    elif self.end and pg.Rect((440, 500, 200, 100)).collidepoint(pg.mouse.get_pos()): # next / again button
                        if sound: self.click.play()
                        if not self.victory: # play again
                            self.end = False
                            pg.mouse.set_visible(False) # Hide cursor here
                        else: # next level
                            self.status = True

        if not self.end: nums = self.draw_grid(self.color, pg.Rect((900, 10, 150, 70)).collidepoint(pg.mouse.get_pos()), pg.mouse.get_pos())
        return self.running, self.status

if __name__ == "__main__":
    running = True
    third = Third()
    while running:
        running, status = third.f(True)
