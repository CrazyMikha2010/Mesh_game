from zero_first import Zero_First
from skibidi import First
from first_second import First_Second
from second import Second
from second_third import Second_Third
from third import Third
from third_fourth import Third_Fourth
from fourth import Fourth
from settings import *

sound, music = True, True
prev_music = True

my_song = pg.mixer.music.load(mainpath + "/sound/song.mp3")
pg.mixer.music.play(-1)

classes = {1: Zero_First(), 2: First(), 3: First_Second(), 4: Second(), 5: Second_Third(), 6: Third(), 7: Third_Fourth(), 8: Fourth()}
cur_class = 1
running = True
while running:
    if cur_class != 1:
        running, won_level = classes[cur_class].f(sound)
    else:
        running, won_level, sound, music = classes[cur_class].f()
        if not music:
            pg.mixer.music.stop()
        if music and not prev_music:
            pg.mixer.music.play(-1)
            prev_music = True
        prev_music = music
    if won_level:
        cur_class = cur_class + 1 if cur_class < 9 else 1

    clock.tick(FPS)
pg.quit()

