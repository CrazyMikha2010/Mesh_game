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

font_xl = pg.font.SysFont('Comic Sans MS', 70)
font_l = pg.font.SysFont('Comic Sans MS', 40)
font_m = pg.font.SysFont('Comic Sans MS', 30)
font_s = pg.font.SysFont('Comic Sans MS', 20)
