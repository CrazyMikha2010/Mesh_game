import os
import pygame as pg
import random
import math

mainpath = os.path.dirname(os.path.abspath(__file__)) # finds path to main.py
pg.init()
pg.font.init()
pg.display.set_caption('Mezhibovskiy project')
clock = pg.time.Clock()
FPS = 60
w, h = 1080, 720
scr = pg.display.set_mode((w, h))

font_path = mainpath + "/Dp_font-Regular 3.ttf"
font_m = pg.font.Font(font_path, 60)
font_xl_num = pg.font.SysFont("Comic Sans", 70)
font_xl = pg.font.Font(font_path, 140)
font_l = pg.font.Font(font_path, 80)
font_s = pg.font.Font(font_path, 40)
font_xs = pg.font.Font(font_path, 20)

class Text_Wrapper:
    def __init__(self):
        ...

    def text_wrapper(self, text, font, width):
        lines = [[]]
        for word in text.split(' '):
            test_line = ' '.join(lines[-1] + [word])
            if font.size(test_line)[0] < width:
                lines[-1].append(word)
            else:
                lines.append([word])
        return lines
