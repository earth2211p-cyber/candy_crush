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
        ellipse(self.pos_x, self.pos_y, self.size, self.size)


def get_candy(grid_size):
    i = 0
    while i < grid_size + 3:
        j = 0
        grid_hold = []
        while j < grid_size + 3:
            grid_hold.append(0)
            j = j + 1
        grid.append(list(grid_hold))
        grid_posx.append(list(grid_hold))
        grid_posy.append(list(grid_hold))
        i = i + 1
        

def fill_candy(grid_x, grid_y):
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
            if grid[i][j] == 0:
                grid[i][j] = random.randint(1,4)
            j = j + 1
        i = i + 1

def draw_grid(grid_x, grid_y):
    x = width / grid_x
    y = (height-100) / grid_y
    i = 1
    while i < grid_x:
        line(i*x,0,i*x,height-100)
        i = i + 1
    i = 1
    while i < grid_y + 1:
        line(0,i*y,width,i*y)
        i = i + 1


def visual(grid_x, grid_y):
    global half_x
    global half_y
    i = 0
    x = width / grid_x
    y = (height-100) / grid_y
    half_x = x/2
    half_y = y/2
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



def three_del(grid_x, grid_y):
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


def is_three_del():
    i = 0
    while i < grid_y:
        j = 0
        while j < grid_x:
            if grid[i][j] != 0:
                if grid[i][j] == grid[i][j+1]:
                    if grid[i][j] == grid[i][j+2]:
                        return True
                if grid[i][j] == grid[i+1][j]:
                    if grid[i][j] == grid[i+2][j]:
                        return True
            j = j + 1
        i = i + 1
    return False


def candy_fall(grid_x, grid_y):
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

def save():
    global grid, grid_x, grid_y
    holder = []
    i = 0
    while i < len(grid) - 3:
        row_string = ""
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 1:
                row_string += "R"
            elif grid[i][j] == 2:
                row_string += "G"
            elif grid[i][j] == 3:
                row_string += "B"
            elif grid[i][j] == 4:
                row_string += "Y"
            j = j + 1
        holder.append(row_string + "\n")
        i = i + 1
    with open("save.txt", "w") as f:   
       f.writelines(holder)
    println("Game Saved!")


def load():
    global grid
    i = 0
    with open("save.txt", "r") as f:
        for line in f:
            line = line.strip()
            j = 0
            while j < len(line):
                if line[j] == "R":
                    grid[i][j] = 1
                elif line[j] == "G":
                    grid[i][j] = 2
                elif line[j] == "B":
                    grid[i][j] = 3
                elif line[j] == "Y":
                    grid[i][j] = 4
                j += 1
            i +=1
    println("Game Loaded!")



def mousePressed():
    global grid_x, grid_y,half_x, half_y
    if mouseY > 420 and mouseY < 480:
        if mouseX > 90 and mouseX < 200:
            save()
        elif mouseX > 300 and mouseY < 410:
            load()
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



def mouseReleased():
    global grid_x, grid_y, half_x, half_y
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
    swap()


def swap():
    global swapholder
    is_adjacent = False
    if swapholder[0][0] == swapholder[1][0]:
        if swapholder[0][1] - 1 == swapholder[1][1] or swapholder[0][1] + 1 == swapholder[1][1]:
            is_adjacent = True
    elif swapholder[0][1] == swapholder[1][1]:
        if swapholder[0][0] - 1 == swapholder[1][0] or swapholder[0][0] + 1 == swapholder[1][0]:
            is_adjacent = True
    if is_adjacent == True:
        candy_holder = grid[swapholder[0][0]][swapholder[0][1]]
        grid[swapholder[0][0]][swapholder[0][1]] = grid[swapholder[1][0]][swapholder[1][1]]
        grid[swapholder[1][0]][swapholder[1][1]] = candy_holder
        if is_three_del() == False:
            candy_holder = grid[swapholder[0][0]][swapholder[0][1]]
            grid[swapholder[0][0]][swapholder[0][1]] = grid[swapholder[1][0]][swapholder[1][1]]
            grid[swapholder[1][0]][swapholder[1][1]] = candy_holder
            swapholder = [[0,0],[0,0]]

def setup():
    global grid_size, grid_x, grid_y, grid_posx, grid_posy, grid, swapholder, half_x, half_y
    grid_size = 10
    grid_x = 10
    grid_y = 10
    grid_posx = []
    grid_posy = []
    grid = []
    swapholder = [[0,0],[0,0]]
    half_x = 0
    half_y = 0
    size(500,500)
    get_candy(grid_size)
    fill_candy(grid_x, grid_y)


def draw():
    global grid_x, grid_y
    background(255)
    textSize(50)
    fill(0)
    text("SAVE", 90, 470)
    textSize(50)
    fill(0)
    text("LOAD", 300, 470)
    draw_grid(grid_x, grid_y)
    visual(grid_x, grid_y)
    three_del(grid_x, grid_y)
    candy_fall(grid_x, grid_y)

