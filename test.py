# import pygame as pg
# import math
# import random

# pg.display.set_caption('Mezhibovskiy project')
# clock = pg.time.Clock()
# FPS = 60
# w, h = 1080, 720
# scr = pg.display.set_mode((w, h))

# pi = math.pi

# center = (w // 2, h // 2)
# r = 350
# divisions = 100
# angle = 360 / divisions
# lev = pg.image.load("5x30.png")
# lev = pg.transform.scale(lev, (600, 700))
# def draw_wheel(rotation):
#     slots = []
#     for i in range(divisions):
#         start = math.radians(i * angle + rotation)
#         end = math.radians((i + 1) * angle + rotation)
#         color = 'black' if i % 2 == 0 else 'red'
#         pg.draw.arc(scr, color, (center[0] - r, center[1] - r, r * 2, r * 2), start, end, r)
#     scr.blit(lev, (190, 0))
#     pg.display.flip()


# running = True
# rotation = 360
# while running:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False

#         if event.type == pg.MOUSEBUTTONDOWN:
#             rotation = 360
#     scr.fill('white')
#     rotation *= 0.99
#     draw_wheel(rotation)

#     clock.tick(FPS)



backstory = "Lonely grasshopper wandering around never-ending fields decides to look for the love of his life. He heard rumours surrounding young princess locked in a tower in desperate wait for brave knight to save her. "
rules = "Now that you’re finally standing next to her tower, you, as every other knight, have to make a brave act: field in front of tower is full of mines. From the top-left corner you can go down or right (using arrow keys). Your goal is to choose the path to the bottom-right corner such that the amount of mines you stepped on is the smallest. After crossing it, fortune will decide whether you’ll get to meet princess, or blow up as other contenders."

tmp_back = []
tmp_rules = []
cnt = 0
prev = 0
for i in range(len(rules)):
    if rules[i] == ' ':
        cnt += 1
        if cnt % 12 == 0:
            tmp_back.append(rules[prev:i])
            prev = i
tmp_back.append(rules[prev:])
print(tmp_back)
