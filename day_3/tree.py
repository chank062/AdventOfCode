# get file split into lines
with open('input.txt') as r:
    lines = r.readlines()

fabric = [ [0 for x in range(1000)] for x in range(1000)]

for line in lines: # for each line
    # split from @, take ' ' off both ends, split at :
    a = line.split('@')[1].strip().split(':')
    b = a[0].split(',') # split by ,
    c = a[1].split('x') # split by x
    x = int(b[0]) # assign pos x
    y = int(b[1]) # assign pos y
    w = int(c[0]) # assign piece width
    h = int(c[1]) # assign piece height
    for i in range(y, y + h): # for the total height of the shape
        for j in range(x, x + w): # for the total width of the shape
            fabric[i][j] +=1

overlap = 0 # overlap counter
for row in range(1000): # for 1000 rows
    for col in range(1000): # for 1000 columns
        if fabric[row][col] >= 2: #
            overlap +=1 # add one to overlap counter
        # if fabric[row][col] == 0:

print("part 1: " + str(overlap)) # 116140
