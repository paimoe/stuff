import sys, random, math

def show_maze(maze):
    for row in maze:
        print(' '.join(row))

if __name__ == '__main__':
    rows = int(sys.argv[1])

    wall_max = rows / 2
    wall_count = random.randrange(1, rows)
    
    cheeses = int(rows / 2)

    # build
    maze = []
    for i in range(0, rows):
        z = []
        for j in range(0, rows):
            z.append('.')
        maze.append(z)
    

    # Add random cheese
    maxcells = rows ** 2
    cheesecells = random.sample(range(1, maxcells), cheeses)
    for ch in cheesecells:
        row = max(0, math.floor(ch / rows) - 1)
        col = max(0, ch - (math.floor(ch) // rows * rows)) # or last digit of ch?
        print(ch, row, col)
        maze[row][col] = 'c'

    show_maze(maze)

    with open('maze.txt', 'w') as f:
        s = "\n".join([''.join(r) for r in maze])
        print(s)
        f.write(s)