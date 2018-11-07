from collections import deque


# Instantiable class to represent a graph
class Graph(object):

    # Initializer: given sets of vertices and edges
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

        # Construct an "adjacency list" representation
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for v,u in edges:
            self.neighbors[v].add(u)
            self.neighbors[u].add(v)

    # Return a string description of this graph
    def __str__(self):
        output = ""
        for v,neighbors in self.neighbors.items():
            output += str(v) + " -> " + str(neighbors) + "\n"
        return output

    # Add all vertices reachable from v to the marks set
    def dfs(self, v, marks):
        marks.add(v)
        for u in self.neighbors[v]:
            if u not in marks:
                self.dfs(u, marks)

    # Map all vertices to their parents along the shortest path from v
    def bfs(self, v, parents):
        parents[v] = v
        frontier = deque()
        frontier.append(v)
        while len(frontier) > 0:
            p = frontier.popleft()
            for c in self.neighbors[p]:
                if c not in parents:
                    parents[c] = p
                    frontier.append(c)

    # Return the shortest path to v from the root of a BFS tree
    @staticmethod
    def path(v, parents):
        if v in parents:
            path = deque([v])
            while v != parents[v]:
                v = parents[v]
                path.appendleft(v)
            return path


def do_tests():

    # Make sets of vertices and edges
    vertices = {1,2,3,4,5,6,7,8,9}
    edges = {(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(5,9),(6,7),(6,8),(7,8)}

    # Construct the graph
    g = Graph(vertices, edges)
    print(g)

    # See all vertices reachable from 1
    marks = set()
    g.dfs(1, marks)
    print(marks)

    # See all vertices reachable from 6
    marks = set()
    g.dfs(6, marks)
    print(marks)

    # See the BFS tree from 1
    parents = dict()
    g.bfs(1, parents)
    print(parents)

    # Use the BFS tree to find shortest paths from 1
    print(Graph.path(9, parents)) # [1,5,9]
    print(Graph.path(6, parents)) # None


if __name__ == '__main__':
    do_tests()
