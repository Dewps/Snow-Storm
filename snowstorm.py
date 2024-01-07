import os
import random
import time

SNOW_DENSITY = 1
SNOW_DELAY = .05
SNOW_FLAKES = ['❆', '❅', '❆', '❉', '*']

term = os.get_terminal_size()

w = term.columns
h = term.lines

grid = []

for _ in range(h):
    grid.append([' '] * w)
    
def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\033[?25l')
    
    output = ''
    
    for row in grid:
        output += ''.join(row) + '\n'
        
    output = output.strip('\n')
    
    print(output, end='')
    
while True:
    row = []
    
    for _ in range(w):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(SNOW_FLAKES))
        else:
            row.append(' ')
        
    grid.insert(0, row)
    grid.pop
        
    draw_grid()
    
    time.sleep(SNOW_DELAY)