import random

class Candy():
    def __init__(self, color, size, pos_x, pos_y):
        self.color = color
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw_candy(self):
        if self.color == 1:
            fill(255,0,0)
        elif self.color == 2:
            fill(0,255,0)
        elif self.color == 3:
            fill(0,0,255)
        elif self.color == 4:
            fill(255,255,0)
        ellipse(self.pos_x,self.pos_y,self.size,self.size)



def setup():
    size(500,500)

def get_candy(grid, grid_size):
    i = 0
    grid_hold = []
    while i < grid_size + 3:
        j = 0
        while j < grid_size + 3:
            grid_hold.append(0)
            j = j + 1
        grid.append(grid_hold)
        grid_hold = []
        i = i + 1
        

def fillin(grid_x, grid_y, matrix):
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
            if matrix[i][j] == 0:
                matrix[i][j] = random.randint(1,4)
            j = j + 1
        i = i + 1

def visaul(grid_x, grid_y, scr_sizex, scr_sizey, matrix):

def three_del(grid_x, grid_y, matrix):

def fall(grid_x, grid_y, matrix):

def mousePressed():

def draw():

