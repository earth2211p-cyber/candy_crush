# ณัฐวรรธน์ อุทัยนฤมล 6901012610013
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
    grid_posx = []
    grid_posy = []
    grid = []
    grid_hold = []
    swapholder = [[0,0],[0,0]]

def get_candy(grid_size):
    i = 0
    while i < grid_size + 3:
        j = 0
        while j < grid_size + 3:
            grid_hold.append(0)
            j = j + 1
        grid.append(grid_hold)
        grid_posx.append(grid_hold)
        grid_posy.append(grid_hold)
        grid_hold = []
        i = i + 1
        

def fillin(grid_x, grid_y, grid):
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
            if grid[i][j] == 0:
                grid[i][j] = random.randint(1,4)
            j = j + 1
        i = i + 1

def draw_grid(grid_x, grid_y, scr_sizex, scr_sizey):
    x = scr_sizex / grid_x
    y = scr_sizey / grid_y
    i = 1
    while i < grid_x:
        line(i*x,0,i*x,scr_sizey)
        i = i + 1
    i = 1
    while i < grid_y:
        line(0,i*y,scr_sizex,i*y)
        i = i + 1


def visual(grid_x, grid_y, scr_sizex, scr_sizey, grid):
    global half_x
    global half_y
    i = 0
    x = scr_sizex / grid_x
    y = scr_sizey / grid_y
    half_x = (scr_sizex / grid_x)/2
    half_y = (scr_sizey / grid_y)/2
    while i < grid_y:
        j = 0
        while j < grid_x:
            if grid[i][j] != 0:
                grid_posx[i][j] = (j+1)*x-half_x
                grid_posy[i][j] = (i+1)*y-half_y
                c = Candy(grid[i][j], 50, (j+1)*x-half_x, (i+1)*y-half_y)
                c.draw_candy()
            j = j + 1
        i = i + 1



def three_del(grid_x, grid_y, grid):
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
            if grid[i][j] != 0:
                if grid[i][j] == grid[i][j+1]:
                    if grid[i][j] == grid[i][j+2]:
                        grid[i][j] = 0
                        grid[i][j+1] = 0
                        grid[i][j+2] = 0
                if grid[i][j] == grid[i+1][j]:
                    if grid[i][j] == grid[i+2][j]:
                        grid[i][j] = 0
                        grid[i+1][j] = 0
                        grid[i+2][j] = 0
            j = j + 1
        i = i + 1


def fall(grid_x, grid_y, grid):
    i = 0
    while i < grid_y:
            j = 0
            while j < grid_x:
                if grid[i][j] == 0:
                    if i == 0:
                        grid[i][j] = random.randint(1,4)
                    else:
                        l = i
                        while l > 0:
                            grid[l][j] = grid[l-1][j]
                            l = l - 1
                        grid[l][j] = random.randint(1,4)
                j = j + 1
            i = i + 1



def mousePressed():
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
        if mouseX > grid_posx[i][j] - half_x and mouseX < grid_posx[i][j] + half_x:
            if mouseY > grid_posy[i][j] - half_y and mouseY < grid_posy[i][j] + half_y:
                swapholder[0][0] = i
                swapholder[0][1] = j 
        j = j + 1
    i = i + 1



def mouseReleased(grid_x, grid_y):
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
        if mouseX > grid_posx[i][j] - half_x and mouseX < grid_posx[i][j] + half_x:
            if mouseY > grid_posy[i][j] - half_y and mouseY < grid_posy[i][j] + half_y:
                swapholder[1][0] = i
                swapholder[1][1] = j 
        j = j + 1
    i = i + 1

def swap():
    candy_holder = 0
    if swapholder[0][0] == swapholder[1][0]:
        if swapholder[0][1] - 1 == swapholder[1][1] or swapholder[0][1] + 1 == swapholder[1][1]:
            candy_holder = grid[swapholder[0][0]][swapholder[0][1]]
            grid[swapholder[0][0], swapholder[0][1]] = grid[swapholder[1][0], swapholder[1][1]]
            grid[swapholder[1][0], swapholder[1][1]] = candy_holder
    elif swapholder[0][1] == swapholder[1][1]:
        if swapholder[0][0] - 1 == swapholder[1][0] or swapholder[0][0] + 1 == swapholder[1][0]:
            candy_holder = grid[swapholder[0][0]][swapholder[0][1]]
            grid[swapholder[0][0], swapholder[0][1]] = grid[swapholder[1][0], swapholder[1][1]]
            grid[swapholder[1][0], swapholder[1][1]] = candy_holder



def draw():

