import collections
from itertools import groupby

Cell = collections.namedtuple('Cell', ['x', 'y', 'value'])

class Maze(object):

    cells = None
    cheeseloc = []

    rowcount = 0
    colcount = 0

    origin = None
    goal = None

    def __init__(self, data, origin=None):
        self.data = data
        self.cells = collections.OrderedDict()

        # Generate cells
        self.rowcount = len(self.data)
        self.colcount = len(self.data) # assume square for now
        for rnum, row in enumerate(self.data):
            for col, val in enumerate(row):
                self.set_cell(rnum, col, val)

                if val == 'c':
                    self.cheeseloc.append((rnum, col))

        if origin is not None:
            self.set_origin(*origin)
            self.pos = origin
    
    def show(self):
        def kf(x):
            return x[1].x
        for k, g in groupby(self.cells.items(), kf):
            print(' '.join([x[1].value for x in g]))

    def cell(self, x, y):
        try:
            return self.cells['{0}_{1}'.format(x, y)]
        except KeyError:
            return None
    def current_cell(self):
        return self.cells['{0}_{1}'.format(self.pos[0], self.pos[1])] 

    def set_cell(self, x, y, val):
        self.cells['{0}_{1}'.format(x, y)] = Cell(x, y, val)

    def set_origin(self, x, y):
        self.origin = (x, y)
        self.set_cell(x, y, 'O')

    def set_goal(self, x, y):
        self.goal = (x, y)
        self.set_cell(x, y, 'G')

    def __len__(self):
        return len(self.cells)

    def cheeses(self):
        return self.cheeseloc

    def has_cheese(self):
        pass

    def adjacent(self, x=None, y=None, ignore=[]):
        # Get adjacent cells
        if x is None and y is None:
            x, y = self.pos
        up = self.cell(x - 1, y)
        ri = self.cell(x, y + 1)
        dn = self.cell(x + 1, y)
        lf = self.cell(x, y - 1)
        print('====')
        print(ignore, up, ri, dn, lf)
        print('====')
        return (
            up if up not in ignore else None,
            ri if ri not in ignore else None,
            dn if dn not in ignore else None,
            lf if lf not in ignore else None
            )

class Path2(object):

    nodes = []
    visited = []
    checkpoints = []

    _c = 0

    def __init__(self, maze):
        self.maze = maze

        self.checkpoints = self.maze.cheeses()

        self.add_point(self.maze.current_cell(), 0)

    def add_point(self, p, distance):
        if (p, distance) not in self.nodes:
            self.nodes.append((p, distance))
            self.visited.append(p)

    def add_points(self, points, distance):
        # ignore points that already exist, with the same or lower weight
        for p in points:
            if (p, distance) not in self.nodes:
                self.nodes.append((p, distance))
                self.visited.append(p)

    def __str__(self):
        return str(self.nodes)

    def current(self):
        r = self.nodes[self._c]
        self._c += 1
        return r

class Path2(object):
    def __init__(self, weight, pos):
        self.weight = weight
        self.pos = pos
    def includes_node(self, cell):
        pass

class PathCollection(object):

    paths = []
    _c = 0

    def __init__(self):
        pass
    def add(self, p, weight):
        self.paths.append(p)
    def exists_or_similar(self, cell):
        # Check to see if this is already on a path, and has an equal or lower weight
        # so we dont add more expensive routes
        pass
    def current(self):
        return self.paths[self._c]


if __name__ == '__main__':
    with open('maze.txt', 'r') as f:
        data = [x.strip("\n") for x in f.readlines()]
    
    # Setup
    start = (0,3)
    goal = (3,3)

    # Construct maze
    maze = Maze(data, start)

    maze.set_goal(*goal)

    #path = Path(maze)
    paths = PathCollection()
    paths.add(maze.current_cell())
    weight = 1

    i = 0
    while True:
        # Start loop. Get adjacent and start calculating scores
        cell = paths.current()
        print('cel', cell)
        adj = maze.adjacent(cell.x, cell.y)
        print('adj', adj)
        # Remove invalid
        for a in adj:
            if a is not None:
                paths.add(a, weight)


        path.add_points(adj, weight)

        if weight == 18:
            break
        weight += 1

    print(path)
    maze.show()