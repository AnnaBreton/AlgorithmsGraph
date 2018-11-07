from heapq import *

from graph import Graph


# Instantiable class to represent a weighted graph

class WeightedGraph(Graph):

    # Initializer: given sets of vertices and edges

    def __init__(self, vertices, edges):

        self.vertices = vertices

        self.edges = edges

        # Construct an "adjacency list" representation

        self.neighbors = dict()

        for v in vertices:
            self.neighbors[v] = set()

        for u, v, w in edges:
            self.neighbors[v].add(u)

            self.neighbors[u].add(v)

        # Allow fast lookup of edge weights

        self.weights = dict()

        for u, v, w in edges:
            self.weights[(u, v)] = w

            self.weights[(v, u)] = w

    # Return a string description of this graph

    def __str__(self):

        output = ""

        for v, neighbors in self.neighbors.items():
            neighbors = {u: self.weights[(v, u)] for u in neighbors}

            output += str(v) + " -> " + str(neighbors) + "\n"

        return output

    # Map all vertices to their parents along the lowest-weight path from v

    # Also map all vertices to their costs along that same path

    def dijkstra(self, v, parents, costs):

        parents[v] = v

        costs[v] = 0

        frontier = [(0, v)]

        off_frontier = set()

        while len(frontier) > 0:

            pcost, p = heappop(frontier)

            if p not in off_frontier:

                off_frontier.add(p)

                for c in self.neighbors[p]:

                    w = pcost + self.weights[(p, c)]

                    if c not in costs or w < costs[c]:
                        parents[c] = p

                        costs[c] = w

                        heappush(frontier, (w, c))

    def prim(self, v, parents):
        print("\n Start Prims: ", v, parents)
        cost = dict()
        parents[v] = v  # mark v as its own parent
        cost[v] = 0  # set cost to 0
        frontier = [(0, v)]  # insert v onto frontier with priority 0
        off_frontier = set()
        while len(frontier) > 0:  # while frontier isn't empty
            print("frontier1 =", frontier)
            pcost, p = heappop(frontier)  # delete min from frontier
            #print("frontier2 =", frontier)
            #print("deleted min from frontier, pcost,  p: ", pcost, p)
            if p not in off_frontier:
                #print(p, " is not in off_frontier p: ", p)
                off_frontier.add(p)  # marks p as finished
                print("Marked ", p, " as finished in off_frontier: ", off_frontier)
                for c in self.neighbors[p]:  # for each unfinished c adjacent to p
                    if c not in off_frontier:  # if c is unfinished
                            #print("  unfinished ", c, " adjacent to p: ", p)
                            w = self.weights[(p, c)]
                            if c not in cost:
                                parents[c] = p  # mark c with parent p and cost w
                                cost[c] = w
                                heappush(frontier, (w, c))  # insert c on frontier with priority w
                            elif cost[c] > w:
                                #print("     cost[c] > w cost[c],w,p,c :", cost[c], w, p, c)
                                #print("     frontier =", frontier)
                                parents[c] = p  # change c with parent p and cost w
                                cost[c] = w
                                #print("doing heapreplace with w,c: ", w, c)
                                heapreplace(frontier, (w, c))
        print(" Parents: ", parents)


def do_tests():
    # Make sets of vertices and edges
    vertices = {'A', 'B', 'C', 'D', 'E', 'F','G',"H","I", "J"}

    edges = {('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),

             ('B', 'D', 3), ('B', 'F', 10), ('C', 'E', 6), ('D', 'E', 2), ('F', 'E', 2),('G','F',2),
             ("I","D",3), ("H","A",3),("J","F",3),}



    # vertices = {'A', 'B', 'C', 'D', 'E','F','G'}


    #edges = {('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),

     #       ('B', 'D', 3), ('B','F',10),('C', 'E', 6), ('D', 'E', 2) , ('F', 'E', 2),('F', 'G', 2), ('G', 'F', 2),('G','B',99)
      #      }

    # Construct the graph

    g = WeightedGraph(vertices, edges)


    print("var links  =[")
    for v1 in g.vertices:
        for n in g.neighbors[v1]:
            print("{source:\"", v1,"\", target:\"",n,"\"},")
    print ("];")



if __name__ == '__main__':
    do_tests()
