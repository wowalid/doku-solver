
all_grids = {}

def add(name, size, *info):
    all_grids[name] = (size, info)

add("first", 4,
    ["8+", (0,0), (0,1), (1,1)],
    ["3=", (1,0)],
    ["8*", (0,2), (1,2), (1,3)],
    ["2=", (0,3)],
    
    ["7+", (2,0), (2,1), (2,2), (3,2)],
    ["8*", (3,0), (3,1)],
    ["1-", (2,3), (3,3)]
    )

add("easy", 5,
    ["9+", (0,0), (1,0), (1,1), (1,2)],
    ["16+", (0,1), (0,2), (0,3), (1,3)],
    ["6*", (0,4), (1,4)],
    
    ["20*", (2,0), (3,0), (2,1), (3,1)],
    ["1-", (2,2), (3,2)],
    ["4+", (2,3), (3,3)],
    ["4=", (2,4)],
    
    ["15*", (4,0), (4,1)],
    ["2=", (4,2)],
    ["10+", (3,4), (4,3), (4,4)]
    )

add("easy2", 5,
    ["60*", (0,0), (0,1), (0,2)],
    ["75*", (1,0), (1,1), (2,0)],
    ["7+", (0,3), (1,3), (1,2)],
    ["1=", (0,4)],
    
    ["7+", (2,1), (2,2), (3,2)],
    ["2/", (1,4), (2,4)],
    ["3=", (2,3)],
    
    ["5+", (3,0), (4,0), (3,1)],
    ["60*", (4,1), (4,2), (4,3), (3,3)],
    ["8+", (3,4), (4,4)]
    )

add("hard", 7,
    ["5=", (2,0)],
    ["2=", (3,2)],
    ["1=", (5,3)],
    
    ["16+", (0,0), (1,0), (1,1)],
    ["15+", (0,1), (0,2), (0,3)],
    ["6+", (0,6), (1,6)],
    ["8+", (3,0), (3,1), (4,1)],
    ["9+", (4,2), (4,3), (3,3)],
    ["23+", (3,5), (3,6), (4,5), (4,6)],
    ["13+", (4,0), (5,0), (6,0)],
    
    ["30*", (1,2), (1,3), (1,4), (0,4)],
    ["7*", (0,5), (1,5)],
    ["42*", (2,1), (2,2), (2,3)],
    ["168*", (2,4), (2,5), (2,6), (3,4)],
    ["18*", (4,4), (5,4)],
    ["336*", (5,1), (5,2), (6,1), (6,2)],
    ["180*", (6,3), (6,4), (6,5), (5,5)],
    
    ["5/", (5,6), (6,6)],
    )

add("veryeeasy", 4,
    ['2=', (1, 0)],
    ['3=', (3, 3)],
    ['2*', (0, 3), (1, 3)],
    ['12*', (2, 2), (2, 3)],
    ['8*', (3, 0), (3, 1), (3, 2)],
    ['6*', (2, 0), (2, 1), (1, 1)],
    ['12+', (0, 0), (0, 1), (0, 2), (1, 2)])

add("reallyhard", 7,
['3=', (2, 1)], ['5=', (1, 3)], ['6=', (5, 4)], ['60*', (0, 0), (0, 1), (0, 2)], ['14+', (0, 3), (0, 4), (1, 4)], ['3+', (0, 5), (1, 5)], ['28*', (0, 6), (1, 6), (2, 6)], ['72*', (1, 0), (1, 1), (1, 2), (2, 2)], ['11+', (2, 4), (2, 5)], ['14+', (2, 0), (3, 0), (4, 0)], ['10+', (2, 3), (3, 3), (3, 4), (3, 5)], ['6+', (3, 1), (4, 1)], ['15+', (3, 2), (4, 2), (4, 3)], ['20+', (3, 6), (4, 4), (4, 5), (4, 6)], ['56*', (5, 0), (6, 0), (5, 1)], ['4*', (5, 2), (5, 3)], ['8+', (6, 1), (6, 2)], ['6/', (6, 3), (6, 4)], ['17+', (5, 5), (6, 6), (5, 6), (6, 5)])

add('unsolvable', 5,
['24*', (0, 0), (1, 0), (2, 0)], ['60*', (0, 1), (0, 2), (0, 3), (1, 1)], ['2=', (0, 4)], ['5/', (1, 4), (2, 4)], ['10+', (2, 2), (1, 2), (1, 3)], ['6+', (3, 3), (2, 3)], ['10+', (3, 0), (3, 1), (2, 1)], ['1=', (4, 0)], ['8+', (3, 2), (4, 2), (4, 1)], ['36*', (4, 4), (4, 3), (3, 4)])

# SUDOKU

add('sudoku-wikipedia', 'sudoku',
*[['5=', (0, 0)], ['3=', (1, 0)], ['6=', (0, 1)], ['9=', (1, 2)], ['8=', (2, 2)], ['8=', (0, 3)], ['4=', (0, 4)], ['7=', (0, 5)], ['6=', (1, 6)], ['7=', (4, 0)], ['1=', (3, 1)], ['9=', (4, 1)], ['5=', (5, 1)], ['6=', (7, 2)], ['6=', (4, 3)], ['8=', (3, 4)], ['3=', (5, 4)], ['2=', (4, 5)], ['3=', (8, 3)], ['1=', (8,4)], ['6=', (8, 5)], ['4=', (3, 7)], ['1=', (4, 7)], ['9=', (5, 7)], ['8=', (4, 8)], ['2=', (6, 6)], ['8=', (7, 6)], ['5=', (8, 7)], ['7=', (7, 8)], ['9=', (8, 8)]])

