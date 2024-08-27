import pygame as pg
import random as rnd
import time
from dataclasses import dataclass

pg.init()

wight, columns, rows = 400, 15, 30
distance=wight // columns
height = distance * rows
grid =[0]*columns * rows
speed = 500
#dua hinh anh vao man hinh
picture=[]
for n in range(8):
    picture.append(pg.transform.scale(pg.image.load(f'T_{n}.jpg'),(distance,distance)))

screen = pg.display.set_mode([wight,height])
pg.display.set_caption('Tetris Game')

#tao su kien
tetroromino_down = pg.USEREVENT + 1
speedup = pg.USEREVENT + 2
pg.time.set_timer(tetroromino_down,speed)
pg.time.set_timer(speedup,500)


#tao hinh cho cac chu cai O,I,J,L,S,Z,T
tetrorominos = [[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0],#O
                [0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],#I
                [0,0,0,0,3,3,3,0,0,0,3,0,0,0,0,0],#J
                [0,0,4,0,4,4,4,0,0,0,0,0,0,0,0,0],#L
                [0,5,5,0,5,5,0,0,0,0,0,0,0,0,0,0],#S
                [6,6,0,0,0,6,6,0,0,0,0,0,0,0,0,0],#Z
                [0,0,0,0,7,7,7,0,0,0,7,0,0,0,0,0]]#T

#tao lop va dinh nghia ham
@dataclass
class tetroromino():
    tetro : list
    row : int = 0
    column : int = 5 #toa do hay vi tri xuat hien lan dau

    def show(self):
        for n, color in enumerate(self.tetro):
            if color >0:
                x=(self.column + n%4)*distance
                y=(self.column + n//4)*distance
                screen.blit(picture[color],(x,y))

    def update(self, r, c):
        self.row += r
        self.column += c

character = tetroromino(tetrorominos[2])
status=True
while status:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            status = False
        if event.type == tetroromino_down:
            character.update(1,0)
        if event.type == speedup:
            speed = int(speed * 0.7)
            pg.time.set_timer(tetroromino_down,speed)
        if event.type ==pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                character.update(0,-1)
            if event.key == pg.K_RIGHT:
                character.update(0,1)
            if event.key == pg.K_DOWN:
                character.update(1,0)
    character.update(1,0)
    screen.fill((128,128,128))
    character.show()
    for n, color in enumerate(grid):
        if color > 0:
            x=n % columns * distance
            y=n// columns * distance
            screen.blit(picture[color], (x,y))
    pg.display.flip()
pg.quit()

