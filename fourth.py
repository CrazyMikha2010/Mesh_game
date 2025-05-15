from settings import *

class Fourth:
    def __init__(self):
        self.grid = [[random.randint(-5, 20) for _ in range(7)] for __ in range(7)]
        self.running = True
        self.x, self.y = 0, 0
        self.color = [[False] * 7 for _ in range(7)]
        self.color[0][0] = True
        self.score = self.grid[0][0]
        self.end = False
        self.rotation = 1440
        self.spin = True
        self.status = False
        self.death = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.click2 = pg.mixer.Sound(mainpath + "/sound/click2.wav")
        self.wheel_sound = pg.mixer.Sound(mainpath + "/sound/fortune-wheel.mp3")
        self.wheel_sound.set_volume(0.5)
        self.auto = pg.mixer.Sound(mainpath + "/sound/aaaaaavtomobiiiil.mp3")
        self.explosion = pg.mixer.Sound(mainpath + "/sound/explosion.mp3")
        self.rects = [pg.Rect((190 + i * 100, 10 + j * 100, 100, 100)) for i in range(7) for j in range(7)]

    def turtle(self):
        n, m = len(self.grid), len(self.grid[0])
        a = [row.copy() for row in self.grid]
        for i in range(0, n):
            for j in range(0, m):
                if i and j:
                    a[i][j] += min(a[i - 1][j], a[i][j - 1])
                elif i:
                    a[i][j] += a[i - 1][j]
                elif j:
                    a[i][j] += a[i][j - 1]

        return a[-1][-1]

    def draw_grid(self, score):
        field = pg.image.load(mainpath + "/images4/4Field.png")
        scr.blit(field, (0, 0))

        transparent_surface = pg.Surface((700, 700), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 200))
        scr.blit(transparent_surface, (190, 10))

        n, m = len(self.grid[0]), len(self.grid)

        for i in range(n):
            for j in range(m):
                font_color = "light green"
                if self.color[i][j]:
                    pg.draw.rect(scr, "light green", (190 + i * 100, 10 + j * 100, 100, 100))
                    font_color = "black"
                pg.draw.rect(scr, "black", (190 + i * 100, 10 + j * 100, 105, 105), 5)
                value = font_xl_num.render(f'{self.grid[i][j]}', False, font_color)
                x = 10 if len(str(value)) == 1 else -10
                scr.blit(value, (215 + 100 * i + x, 10 + j * 100))
        score = font_m.render(f'Score:{score if score >= 0 else ';' + str(abs(score))}', False, "black")
        scr.blit(score, (0, 0))

        grasshopper = pg.image.load(mainpath + "/images4/4Grasshopper.png").convert_alpha()
        grasshopper = pg.transform.scale(grasshopper, (120, 80))
        scr.blit(grasshopper, (self.x * 100 + 190, self.y * 100 + 20))

        pg.display.flip()

    def end_scr(self, scr, res):
        minn = self.turtle()

        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 200))
        scr.blit(transparent_surface, (0, 0))

        percent = int(minn / res * 100)

        pg.display.flip()
        return percent


    def wheel(self, percent, rotation, slots):
        living1 = font_m.render('Chance of living:', False, "white")
        living2 = font_m.render(f'{percent} percent', False, "white")
        scr.blit(living1, (700, 0))
        scr.blit(living2, (760, 40))

        center = (w // 2, h // 2)
        r = 350
        divisions = 100
        angle = 360 / divisions
        for i in range(divisions):
            start = math.radians(i * angle + rotation)
            end = math.radians((i + 1) * angle + rotation)
            color = "green" if slots[i] else "blue"
            pg.draw.arc(scr, color, (center[0] - r, center[1] - r, r * 2, r * 2), start, end, r)

        pg.draw.polygon(scr, "red", ((880, 360), (990, 300), (990, 420)))
        life = font_m.render('Life', False, "white")
        death = font_m.render('Death', False, "white")
        pg.draw.rect(scr, "green", (10, 600, 110, 40))
        scr.blit(life, (10, 600))
        pg.draw.rect(scr, "blue", (10, 650, 110, 40))
        scr.blit(death, (10, 650))

        pg.display.flip()

    def handle_mousePress(self, event_pos, sound):
        if self.death:
            if pg.Rect((840, 10, 200, 100)).collidepoint(event_pos):
                if sound: self.click.play()
                self.end = False
                self.x, self.y = 0, 0
                self.color = [[False] * 7 for _ in range(7)]
                self.color[0][0] = True
                self.rotation = 1440
                self.spin = True
                self.score = self.grid[0][0]
        else:
            for rect in self.rects:
                if rect.collidepoint(event_pos):
                    pressed_x, pressed_y = (event_pos[0] - 190) // 100, (event_pos[1] - 10) // 100
                    if any(
                        (all((pressed_x == self.x, pressed_y - self.y == 1)),
                        all((pressed_y == self.y, pressed_x - self.x == 1)))
                        ):
                        if sound: self.click2.play()
                        self.x, self.y = pressed_x, pressed_y
                        self.color[self.x][self.y] = True
                        self.score += self.grid[self.x][self.y]
                        
    def handle_keyDown(self, event_key, sound):
        if event_key == pg.K_DOWN and self.y < 6:
            if sound: self.click2.play()
            self.y += 1
            self.color[self.x][self.y] = True
            self.score += self.grid[self.x][self.y]
        elif event_key == pg.K_RIGHT and self.x < 6:
            if sound: self.click2.play()
            self.x += 1
            self.color[self.x][self.y] = True
            self.score += self.grid[self.x][self.y]

    def draw_screen_main(self, sound):
        if not self.end: 
            scr.fill('white')
            self.draw_grid(self.score)

        if self.x == 6 and self.y == 6 and not self.end: # bottom right corner
            self.end = True
            self.percent = self.end_scr(scr, self.score)
            self.slots = [True] * self.percent + [False] * (100 - self.percent)
            random.shuffle(self.slots)
        if self.end:
            if self.spin: 
                self.wheel(self.percent, self.rotation, self.slots)
                if sound: self.wheel_sound.play()
            if self.rotation > 0.9:
                self.rotation *= 0.99
            elif self.spin == True:
                self.spin = False
                col = scr.get_at((879, 360))
                if sound: self.wheel_sound.stop()
                if col[1] == 255:
                    if sound: self.auto.play()
                    self.death = False
                    happy_end = pg.image.load(mainpath + "/menu/TheEnd.png")
                    scr.blit(happy_end, (0, 0))
                    pg.display.flip()
                else:
                    if sound: self.explosion.play()
                    self.death = True
                    explosion = pg.image.load(mainpath + "/images4/4Death.png")
                    scr.blit(explosion, (0, 0))
                    again = pg.image.load(mainpath + "/images/Again-transp-2.png").convert_alpha()
                    again = pg.transform.scale(again, (200, 100))
                    scr.blit(again, (840, 10))
                    pg.display.flip()

    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mousePress(event.pos, sound)

            elif event.type == pg.KEYDOWN:
                self.handle_keyDown(event.key, sound)

        self.draw_screen_main(sound)
        return self.running, self.status


if __name__ == "__main__":
    running = True
    fourth = Fourth()
    while running:
        running, status = fourth.f(True)
        clock.tick(FPS)
    

