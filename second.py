from settings import *

class Second:
    def __init__(self):
        self.cur = 0
        self.lillys = [0] + [random.randint(-9, 10) for _ in range(8)] + [0]
        self.cnt = 0
        self.masks, self.rects, self.coords1, self.grasshopper = self.draw_screen(self.cnt, self.cur, self.lillys)
        self.running = True
        self.end = False
        self.status = False
        self.jump = pg.mixer.Sound(mainpath + "/sound/jump.mp3")
        self.jump.set_volume(0.1)
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        

    def draw_screen(self, cnt, cur, lillys):
        pond = pg.image.load(mainpath + "/images2/2Pond.png")
        grasshopper = pg.image.load(mainpath + "/images2/Grasshopper2.png").convert_alpha()
        grasshopper = pg.transform.scale(grasshopper, (130, 91))
        lillypad = pg.image.load(mainpath + "/images2/Lillypad2.png").convert_alpha()
        lillypad = pg.transform.scale(lillypad, (150, 100))

        scr.blit(pond, (0, 0))
        coords1 = [(-10, 200), (94, 364), (242, 253), (347, 379), (462, 220), (543, 373), (682, 227), (733, 458), (883, 290), (926, 486)]
        coords2 = [(84, 347), (215, 346), (352, 368), (452, 347), (545, 358), (672, 347), (752, 410), (852, 412), (944, 447), (950, 1000)]
        coords3 = [(66, 312), (104, 381), (184, 373), (239, 328), (326, 349), (367, 393), (431, 382), (471, 319), (531, 327), (561, 382), (642, 379), (691, 322), (739, 354), (758, 454), (827, 458), (874, 377), (936, 400), (959, 483), (950, 1000), (950, 1000)]
        self.masks = {}
        self.rects = {}
        score = font_m.render(f'Lillys count:{cnt if cnt >= 0 else ';' + str(abs(cnt))}', False, "white")
        scr.blit(score, (0, 0))
        
        for i in range(len(lillys)):
            pg.draw.circle(scr, "#7CFC00", coords2[i], 20)
            pg.draw.circle(scr, "#2E8B57", coords3[i * 2], 10)
            pg.draw.circle(scr, "dark green", coords3[i * 2 + 1], 7)
            scr.blit(lillypad, coords1[i])

            mask = pg.mask.from_surface(lillypad)
            rect = grasshopper.get_rect(topleft=coords1[i])
            self.masks[i] = mask
            self.rects[i] = rect
        
        for i in range(1, len(self.lillys) - 1):
            y = -50 if i % 2 == 0 else 100
            x = 20
            cur_lily = self.lillys[i]
            cnt = font_l.render(f'x{cur_lily if cur_lily >= 0 else ';' + str(abs(cur_lily))}', False, "black")
            scr.blit(cnt, (coords1[i][0] + x, coords1[i][1] + y))
        scr.blit(grasshopper, coords1[cur])
        pg.display.flip()

        return self.masks, self.rects, coords1, grasshopper

    def grasshopper_k(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2]) + nums[i]
        return(dp[-1])


    def end_scr(self, scr, res):
        score = self.grasshopper_k(self.lillys) + self.lillys[0]
        if score == res:
            self.victory = True
        else: 
            self.victory = False
        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))

        if self.victory:
            good_boy = pg.image.load(mainpath + "/images2/2Goodboy.png").convert_alpha()
            next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
            next = pg.transform.scale(next, (200, 100))
            scr.blit(good_boy, (0, 0))
            scr.blit(next, (440, 500))
        else:
            bad_boy = pg.image.load(mainpath + "/images2/2Badboy.png").convert_alpha()
            again = pg.image.load(mainpath + "/images/Again-transp-2.png").convert_alpha()
            again = pg.transform.scale(again, (200, 100))
            scr.blit(bad_boy, (0, 0))
            scr.blit(again, (440, 500))
        pg.display.flip()

        return self.victory
    
    def handle_mousePress(self, event_pos, sound):
        if not self.end:
            for i in range(self.cur + 1, self.cur + 3):
                if i < 10 and self.rects[i].collidepoint(event_pos):
                    self.offset_x_mouse = event_pos[0] - self.rects[i].x
                    self.offset_y_mouse = event_pos[1] - self.rects[i].y
                    if self.masks[i].get_at((self.offset_x_mouse, self.offset_y_mouse)):
                        scr.blit(self.grasshopper, self.coords1[i])
                        self.cnt += self.lillys[i]
                        self.cur = i
                        if sound: self.jump.play()
        elif self.end and pg.Rect((440, 500, 200, 100)).collidepoint(pg.mouse.get_pos()): # next / again button
            if not self.victory: # play again
                if sound: self.click.play()
                self.end = False
                self.cur = 0
                self.cnt = 0
            else: # next level
                if sound: self.click.play()
                self.status = True

    def draw_screen_main(self):
        if self.cur == 9:
            self.end = True
            self.victory = self.end_scr(scr, self.cnt)
            self.cur = 0

        if not self.end: self.draw_screen(self.cnt, self.cur, self.lillys)
    
    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mousePress(event.pos, sound)
        
        self.draw_screen_main()
        return self.running, self.status

if __name__ == "__main__":
    running = True
    second = Second()
    while running:
        running, status = second.f(True)
    pg.quit()

