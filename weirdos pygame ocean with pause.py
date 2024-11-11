import pygame
import numpy as np
import random 
import itertools

# ---------------------------------------------------------------------------------
# Define global variables up here
col_pollution = (255 ,0 ,0)
col_alive = (0, 255, 0)
col_background = (89, 0, 179)
# col_background = (10, 10, 40)
col_grid = (30, 30, 60)
life = 11
pollution = 77
nbr = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
gamecycles = 0
toggle = itertools.cycle([life, pollution,0]).__next__
toggle2 = itertools.cycle([col_alive,col_pollution,col_background]).__next__
# ---------------------------------------------------------------------------------
# update function will be where we do our neighbor checking logic
def update(surface, ocean, sz):
    theiceage = np.zeros((ocean.shape[0], ocean.shape[1]))
    # in our previous code we wrote loops i,j in range, the below line lets you loop r,c through
    # the range of the array, eliminating the need for our outer two loops
    # current=random.randint(-1,1)
    # current2=random.randint(-1,1)

    for r, c in np.ndindex(ocean.shape):
        current=random.randint(-1,1)
        current2=random.randint(-1,1)
        # this is where you will loop and check for pollution and nearby neighbors
        # this loop also assigns colors for the individual cells, we currently use polution/alive/background colors
        death = 0
        if ocean[r,c] == life:
            
            for a in nbr:
                if ocean[(r+a[0])%len(ocean),(c+a[1])%len(ocean[0])] == pollution:
                    death=death+1
                                
            if death == 0:
                if theiceage[(r+current)%len(ocean),(c+current2)%len(ocean[0])]==life:
                    theiceage[(r,c)]=life
                    col=col_alive
                else:
                    theiceage[(r+current)%len(ocean),(c+current2)%len(ocean[0])]=life
                    col=col_alive
            else:
                col = col_background

        elif ocean[r,c] == pollution:
                #keep polution in it's place
                theiceage[(r,c)]=pollution
                col = col_pollution
        else:
            col = col_background

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1)) #leave this line alone!

    return theiceage # this is the enf of the update() function
# ---------------------------------------------------------------------------------
# init() function is where we will generate our initial state array, that is random.
# note that it has arguements pushed into it (dimx,dimy) so those are the size of the array
def init(dimx, dimy):
    ocean = np.zeros((dimy, dimx))
    # #randomly assign creatures to ocean, 10% chance
    for y in range(dimy):
        for z in range(dimx): 
            test=random.randint(0,9)
            if test == 1:
                ocean[y,z]=life

    # random pollution creation - top 3 rows only
    for y in range(0,3,1):
        for z in range(dimx):
            test=random.randint(1,100)
            if test <51: # percentage changeable
                ocean[y,z]=pollution

    # random pollution creation - bottom 2 rows
    for y in range(dimy-2,dimy,1):
        for z in range(dimx):
            test=random.randint(1,100)
            if test <51: # percentage changeable
                ocean[y,z]=pollution
    return ocean

# ---------------------------------------------------------------------------------
# main game loop, we can count loops here with a variable and display them inside of this function
def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("the awesome penguin ocean sim.") #we can update title to show lives later

    cells = init(dimx, dimy)
    gamecycles = 0
    paused=False

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type ==pygame.MOUSEBUTTONDOWN: #attempting to click and change cell value in real time
                alive=0
                y,x=event.pos
                print(x//cellsize, " ", y//cellsize)
                cells[x//cellsize,y//cellsize]=toggle()
                for i in range(dimx):
                    for j in range(dimy):
                        if cells[i,j]==life:
                            alive=alive+1
                pygame.display.set_caption(f"the awesome penguin ocean sim. cycle {gamecycles}, Live count {alive}")
                pygame.draw.rect(surface, toggle2(), (x*cellsize, y*cellsize, cellsize-1, cellsize-1))  # this line not updating in real time
                pygame.display.update() #unsure if this is working either, but whatever
            elif event.type == pygame.QUIT:
                pygame.quit()
                return
        if not paused:
            alive=0
            surface.fill(col_grid)
            cells = update(surface, cells, cellsize)
            pygame.time.delay(50) #game speed in milliseconds
            gamecycles = gamecycles+1
            for i in range(dimx):
                for j in range(dimy):
                    if cells[i,j]==life:
                        alive=alive+1
            pygame.display.set_caption(f"the awesome penguin ocean sim. cycle {gamecycles}, Live count {alive}")    
            pygame.display.update()
            if alive==0:
                print("all life ended after ",gamecycles,"gamecycles.")
                pygame.quit()
                return
                                   


# ---------------------------------------------------------------------------------
# this starts the game and defines game board size
if __name__ == "__main__":
    for s in range(1): #for display at competition, we can keep the game looping!
        main(40, 40 , 25) #rows, columns, and pixel size for each cell
