from settings import *

class First:
    def __init__(self):
        self.running = True
        self.dragging = False
        self.offset_x, self.offset_y = 0, 0
        self.victory = None
        self.end = False
        self.images = self.load_images()
        self.rects, self.masks, self.coords = self.setup_objects(self.images)
        self.status = False
        self.click = pg.mixer.Sound(mainpath + "/sound/click.wav")
        self.grasshopper_x, self.grasshopper_y = 0, 0
        self.up = True
        self.m, self.c = [random.randint(1, 10) for _ in range(5)], [random.randint(1, 10) for _ in range(5)]
        self.M = random.randint(10, 20)
        self.stats = {"butterfly": [], "caterpillar": [], "drink": [], "flower": [], "leaf": []} # [weight, price]
        for weight, price, name in zip(self.m, self.c, self.stats.keys()):
            self.stats[name] = [weight, price]

    def backpack(self):
        N = 5
        dp = [0] * (self.M + 1)
        for i in range(N):
            weight, price = self.m[i], self.c[i]
            for j in range(self.M, weight - 1, -1):
                if j >= weight:
                    dp[j] = max(dp[j], dp[j - weight] + price)
        return dp[-1]

    def load_images(self):
        carpet = pg.image.load(mainpath + "/images/Carpet.png").convert_alpha()
        table = pg.image.load(mainpath + "/images/Table.png").convert_alpha()
        grasshopper = pg.image.load(mainpath + "/images/Grasshopper.png").convert_alpha()
        plate = pg.image.load(mainpath + "/images/Plate.png").convert_alpha()

        butterfly = pg.image.load(mainpath + "/images/1Butterfly.png").convert_alpha()
        butterfly = pg.transform.scale(butterfly, (150, 150))
        caterpillar = pg.image.load(mainpath + "/images/1Caterpillar.png").convert_alpha()
        caterpillar = pg.transform.scale(caterpillar, (100, 100))
        drink = pg.image.load(mainpath + "/images/1Drink.png").convert_alpha()
        drink = pg.transform.scale(drink, (200, 200))
        flower = pg.image.load(mainpath + "/images/1Flower.png").convert_alpha()
        flower = pg.transform.scale(flower, (150, 150))
        leaf = pg.image.load(mainpath + "/images/1Leaf.png").convert_alpha()
        leaf = pg.transform.scale(leaf, (350, 350))

        return {"carpet": carpet, "table": table, "grasshopper": grasshopper, "plate": plate, "butterfly": butterfly, "caterpillar": caterpillar, "drink": drink, "flower": flower, "leaf": leaf}


    def setup_objects(self, images):
        coords = {"butterfly": [100, 500], "caterpillar": [300, 500], "drink": [400, 500], "flower": [250, 600], "leaf": [500, 500]}

        rects = {}
        masks = {}
        for name, image in images.items():
            if name in coords:
                rect = image.get_rect(topleft=coords[name])
                mask = pg.mask.from_surface(image)
                rects[name] = rect
                masks[name] = mask

        return rects, masks, coords

    def draw_screen(self, scr, images, rects, weightt, valuee, hover):
        scr.fill("#e7f8de")
        scr.blit(images["carpet"], (0, 0))
        scr.blit(images["grasshopper"], (self.grasshopper_x, self.grasshopper_y))
        self.grasshopper_y += 0.3 if self.up else -0.3
        if abs(self.grasshopper_y) >= 5:
            self.up = not self.up
        self.grasshopper_x += 0.2 if not self.up else -0.2
        scr.blit(images["table"], (0, 0))
        scr.blit(images["plate"], (0, 0))

        oranges = {"butterfly": [25, 35, 65, 30], "caterpillar": [40, 20, 40, 35], "drink": [105, 35, 60, 25], "flower": [10, 30, 60, 25], "leaf": [155, 125, 40, 35]}
        for name, rect in rects.items():
            scr.blit(images[name], rect.topleft)
            orange = oranges[name]
            pg.draw.rect(scr, "#DD7200", (rect.topleft[0] + orange[0], rect.topleft[1] + orange[1], orange[2], orange[3]))
            weight = font_xs.render(f"{self.stats[name][0]}g", False, "black")
            price = font_xs.render(f"{self.stats[name][1]}pr", False, "black")
            scr.blit(weight, (rect.topleft[0] + orange[0], rect.topleft[1] + orange[1]))
            scr.blit(price, (rect.topleft[0] + orange[0] + orange[2] // 2, rect.topleft[1] + orange[1] + orange[3] // 2))



        capacity = font_s.render(f'Capacity: {self.M}g', False, (0, 0, 0))
        weight = font_s.render(f'Weight: {weightt}g', False, (0, 0, 0))
        value = font_s.render(f'Value: {valuee}pr', False, (0, 0, 0))

        scr.blit(capacity, (0, -3))
        scr.blit(weight, (0, 20))
        scr.blit(value, (0, 43))
        
        warning = font_m.render('Weight too big', False, (255, 0, 0))
        if weightt > self.M:
            scr.blit(warning, (400, 0))

        # submit button in top right corner
        x = 20 if hover else 0
        background_color = (127 - x, 127 - x, 127 - x)
        font_color = (0, 0, 0)
        if weightt > self.M:
            background_color = (255 - x, 0, 0)
            font_color = (255, 255, 255)
        elif weightt > 0:
            background_color = (0, 255 - x, 0)
            font_color = (255, 255, 255)

        submit = font_l.render('submit', False, font_color)
        pg.draw.rect(scr, background_color, (900, 5, 150, 70), border_radius=10)
        scr.blit(submit, (910, 10))
        pg.display.flip()

    def check_collision(self, scr, images, masks, rects):
        plate_mask = pg.mask.from_surface(images["plate"])
        plate_rect = images["plate"].get_rect(topleft=(0, 0))
        weight, value = 0, 0
        for name, mask, rect in zip(masks.keys(), masks.values(), rects.values()):
            tmp_offset_x = plate_rect.x - rect.x
            tmp_offset_y = plate_rect.y - rect.y
            if mask.overlap(plate_mask, (tmp_offset_x, tmp_offset_y)):
                weight += self.stats[name][0]
                value += self.stats[name][1]
        return weight, value

    def end_scr(self, scr):
        weight, value = self.check_collision(scr, self.images, self.masks, self.rects)
        if self.backpack() == value:
            self.victory = True
        else: 
            self.victory = False
        transparent_surface = pg.Surface((1080, 720), pg.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 128))
        scr.blit(transparent_surface, (0, 0))

        if self.victory:
            good_boy = pg.image.load(mainpath + "/images/1Goodboy.png").convert_alpha()
            next = pg.image.load(mainpath + "/images/Next-transp-2.png").convert_alpha()
            next = pg.transform.scale(next, (200, 100))
            scr.blit(good_boy, (0, 0))
            scr.blit(next, (440, 500))
        else:
            bad_boy = pg.image.load(mainpath + "/images/1Badboy.png").convert_alpha()
            again = pg.image.load(mainpath + "/images/Again-transp-2.png").convert_alpha()
            again = pg.transform.scale(again, (200, 100))
            scr.blit(bad_boy, (0, 0))
            scr.blit(again, (440, 500))
        pg.display.flip()

        return self.victory
    
    def f(self, sound):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if pg.Rect((900, 10, 150, 70)).collidepoint(pg.mouse.get_pos()) and not self.end: # submit button press
                    weight, value = self.check_collision(scr, self.images, self.masks, self.rects)
                    if sound: self.click.play()
                    if 0 < weight <= self.M:
                        self.end = True
                        self.victory = self.end_scr(scr)
                
                elif self.end and pg.Rect((440, 500, 200, 100)).collidepoint(pg.mouse.get_pos()): # next / again button
                    if sound: self.click.play()
                    if not self.victory: # play again
                        self.end = False
                    else: # next level
                        self.status = True
                    
                else:
                    for name, rect in self.rects.items():
                        if rect.collidepoint(event.pos):
                            self.offset_x_mouse = event.pos[0] - rect.x
                            self.offset_y_mouse = event.pos[1] - rect.y
                            if self.masks[name].get_at((self.offset_x_mouse, self.offset_y_mouse)):
                                if sound: self.click.play()
                                self.dragging = name
                                self.offset_x, self.offset_y = self.offset_x_mouse, self.offset_y_mouse
                                break
            
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.dragging = None

            elif event.type == pg.MOUSEMOTION:
                if self.dragging:
                    self.rects[self.dragging].topleft = (event.pos[0] - self.offset_x,  event.pos[1] - self.offset_y)

        weight, value = self.check_collision(scr, self.images, self.masks, self.rects)
        if not self.end: self.draw_screen(scr, self.images, self.rects, weight, value, pg.Rect((900, 10, 150, 70)).collidepoint(pg.mouse.get_pos()))

        return self.running, self.status
    

if __name__ == "__main__":
    first = First()
    running = True
    while running:
        running, status = first.f(True)
    pg.quit()
