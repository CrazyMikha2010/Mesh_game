from settings import *

class Zero_First:
    def __init__(self):
        self.running = True
        self.SOUND = True
        self.MUSIC = True
        self.menu = True
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.grasshopper_x, self.grasshopper_y = 540, 360
        self.up = True


    def draw_menu(self, pos, MUSIK, SOUND):
        background = pg.image.load(mainpath + "/menu/Menu.png")
        scr.blit(background, (0, 0))

        transparent_surface = pg.Surface((440, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))

        grasshopper = pg.image.load(mainpath + "/images2/Grasshopper2.png").convert_alpha()
        grasshopper = pg.transform.scale(grasshopper, (130, 91))

        scr.blit(grasshopper, (self.grasshopper_x, self.grasshopper_y))
        self.grasshopper_y += 0.3 if self.up else -0.3
        if abs(360 - self.grasshopper_y) >= 5:
            self.up = not self.up
        self.grasshopper_x += 0.3 if not self.up else -0.3
        
        play = font_xl.render('PLAY', False, "white")
        x = 10 if pg.Rect(40, 200, 330, 100).collidepoint(pos) else 0
        pg.draw.rect(scr, "black", (40, 200, 330 + x, 100 + x))
        scr.blit(play, (50, 200))

        x = 10 if pg.Rect(40, 330, 190, 60).collidepoint(pos) else 0
        color = "black" if MUSIK else "gray"
        music = font_m.render('MUSIC', False, "white")
        pg.draw.rect(scr, color, (40, 330, 190 + x, 60 + x))
        scr.blit(music, (45, 330))

        sound = font_m.render('SOUNDS', False, "white")
        x = 10 if pg.Rect(40, 410, 190, 60).collidepoint(pos) else 0
        color = "black" if SOUND else "gray"
        pg.draw.rect(scr, color, (40, 410, 190 + x, 60 + x))
        scr.blit(sound, (40, 410))

        pg.display.flip()


    def backstory_screen(self):
        background = pg.image.load(mainpath + "/menu/Menu.png")
        scr.blit(background, (0, 0))

        grasshopper = pg.image.load(mainpath + "/images2/Grasshopper2.png").convert_alpha()
        grasshopper = pg.transform.scale(grasshopper, (130, 91))

        scr.blit(grasshopper, (random.randint(270, 275), random.randint(510, 515)))

        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 100))
        scr.blit(transparent_surface, (0, 0))

        backstory = "Lonely grasshopper wandering around never;ending fields decides to look for the love of his life. He heard rumours surrounding young princess locked in a tower in desperate wait for brave knight to save her. "
        rules = "First, to prepare for his way, grasshopper wants to eat a champion breakfast. His belly fits only up to 10 grams. Help him get as much protein as possible, putting stuff he’ll eat in a plate. "

        backstory_lines = Text_Wrapper.text_wrapper(self, backstory, font_m, 1000)
        for i in range(len(backstory_lines)):
            backstory_scr = font_m.render(' '.join(backstory_lines[i]), False, "white")
            scr.blit(backstory_scr, (30 if i > 0 else 60, 20 + 40 * i))
        rules_lines = Text_Wrapper.text_wrapper(self, rules, font_m, 1000)
        for i in range(len(rules_lines)):
            rules_scr = font_m.render(' '.join(rules_lines[i]), False, "white")
            scr.blit(rules_scr, (30 if i > 0 else 60, 220 + 40 * i))

        next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
        next = pg.transform.scale(next, (200, 100))
        scr.blit(next, (440, 500))
        
        pg.display.flip()

    def f(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if pg.Rect(40, 200, 330, 100).collidepoint(event.pos): # play
                    self.backstory_screen()
                    self.menu = False
                    if self.SOUND: self.click.play()

                elif pg.Rect(40, 330, 190, 60).collidepoint(event.pos): # musik
                    self.MUSIC = not self.MUSIC
                    if self.SOUND: self.click.play()

                elif pg.Rect(40, 410, 190, 60).collidepoint(event.pos): # sound
                    self.SOUND = not self.SOUND
                    if self.SOUND: self.click.play()

                elif not self.menu and pg.Rect(440, 500, 200, 100).collidepoint(event.pos): # first level
                    self.status = True
                    if self.SOUND: self.click.play()
        
        
        if self.menu: self.draw_menu(pg.mouse.get_pos(), self.MUSIC, self.SOUND)
        if not self.menu: self.backstory_screen()
        return self.running, self.status, self.SOUND, self.MUSIC

if __name__ == "__main__":
    running = True
    zf = Zero_First()
    while running:
        running, status, sound, music = zf.f()
            

