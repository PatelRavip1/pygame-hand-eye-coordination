import pygame as pg
from random import randint
from time import sleep as s
from time import perf_counter as pf
a = 10
b = 6
turns = 30
scl = 100
t2,t1 = 0,0
screen = pg.display.set_mode((scl*a,scl*b))
running = True
count_avg = []
flag = 1
count = 0
while running:
    if count == turns+1:
        break
    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = 0
    screen.fill(((0,0,0)))
    if flag == 1:
        x = randint(0,a-1)
        y = randint(0,b-1)
        pg.draw.rect(screen,(255,0,0),(x*scl,y*scl,scl,scl))
        pg.display.flip()
        t1 = pf()
        flag = 0
    mouse1 = pg.mouse.get_pressed()
    if mouse1[0] == 1:
        mouse = pg.mouse.get_pos()
        if (x == mouse[0]//scl and y == mouse[1]//scl):
            flag = 1
            t2 =pf()
            count_avg.append(t2-t1)
            count = count +1
        else:
            pass
count_avg = count_avg[1:]
screen.fill(((0,0,0)))
pg.display.flip()
print("avG == ",int(sum(count_avg)/len(count_avg)*1000))
for i in range(10):
    print((i+1),"=" ,int(count_avg[i]*1000),"ms","   ",(i+11),"=" ,int(count_avg[i+10]*1000),"ms","   ",(i+21),"=" ,int(count_avg[i+20]*1000),"ms")
##for i in range(10):
##    print((i+1),"=" ,int(count_avg[i]*1000),"ms","   ",(i+11),"=" ,int(count_avg[i+10]*1000),"ms","   ",(i+21),"=" ,int(count_avg[i+20]*1000),"ms")
##print("avG == ",int((sum(count_avg)/len(count_avg))*1000),"ms")
