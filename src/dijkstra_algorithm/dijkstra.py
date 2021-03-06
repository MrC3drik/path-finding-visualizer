import sys
from src.utils.default_structure import Default


class Dijkstra(Default):
    """[summary]

    Args:
        Default ([type]): [description]
    """


    def __init__(self, table):
        self.non_visited_nodes = []
        self.lowest_distance = {}
        self.previous_node = {}

        super().__init__(table) 

        # set up variables
        for line in self.table:
            for node in line:
                if not node.startswith('wall'):
                    self.non_visited_nodes.append(node)
                    self.lowest_distance[node] = sys.maxsize
                    self.previous_node[node] = None
        self.lowest_distance[self.table[self.start[0]][self.start[1]]] = 0
        

    def run(self):        # run algorithm
        minimum = self.get_minimum_distance_node()
        if minimum:
            minimum_coords = self.get_coordinates(minimum)
            minimum_distance = self.lowest_distance[minimum]

            res = self.check_nodes(minimum, minimum_distance, minimum_coords)
            if res:
                print(f'SUCCESS: found {self.table[res[0]][res[1]]}\nSHORTEST PATH: {self.get_path(res)}')
                return True

            if minimum_coords == self.goal:
                print(f'SUCCESS: found {minimum}\nSHORTEST PATH: {self.get_path(minimum_coords)}')
                return True

            self.non_visited_nodes.remove(minimum)

            return False
            
        else:
            return None


    def get_minimum_distance_node(self):
        try:
            l = [k for k in self.lowest_distance.keys() if k in self.non_visited_nodes and self.lowest_distance[k] < sys.maxsize]
            li = [self.lowest_distance[k] for k in l]

            minimum_index = li.index(min(li))
            minimum = l[minimum_index]

            return minimum

        except:
            return None


    def check_nodes(self, num, min_dist, min_coords):    
        try:   
            x = min_coords[0]
            y = min_coords[1]-1
            node = self.table[x][y]
            if node and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:
            x = min_coords[0]
            y = min_coords[1]+1
            node = self.table[x][y]
            if node and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:    
            x = min_coords[0]+1
            y = min_coords[1]
            node = self.table[x][y]
            if node and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:
            x = min_coords[0]-1
            y = min_coords[1]
            node = self.table[x][y]
            if node and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        return None


    def check_node(self, num, min_dist, coords):
        node = self.table[coords[0]][coords[1]]
        if min_dist + 1 < self.lowest_distance[node]:
            self.lowest_distance[node] = min_dist + 1
            self.previous_node[node] = num


    def get_path(self, coords):
        node = self.table[coords[0]][coords[1]]
        path = []
        while node != self.table[self.start[0]][self.start[1]]:
            path.append(node)
            node = self.previous_node[node]
        path.append(node)

        self.path = path
        return(path)