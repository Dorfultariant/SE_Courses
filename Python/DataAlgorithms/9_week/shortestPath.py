class Graph:

    def __init__(self, n):
        self.N = n
        self.graph = [[0] * self.N for i in range(self.N)]
        #self.list = [[] for i range(self.N)]

    def add(self, u, v, w):
        self.graph[u][v] = w
        #self.list[u].append((v,w))

    def remove(self, u, v):
        self.graph[u][v] = 0
        #if v in self.list[u]:
            #self.list[u].remove()
    

    def printer(self):
        for i in range(self.N):
            for j in range(self.N):
                print(f"{self.graph[i][j]:3d}", end="")
            print()
            

    def shortest_path(self, start, end):
        distance = [float('inf')] * self.N
        previous = [None] * self.N
        queue = [i for i in range(self.N)]

        distance[start] = 0

        while queue:
            u = self.minVertex(queue, distance)
            #print(u)
            # Vertex with shortest distance remaining in queue is removed from queue
            queue.remove(u)

            for v in range(self.N):
                ## this checks that there indeed is an edge between vertices u and v
                if self.graph[u][v] != 0:

                    # Distance (weight) from current u vertex to v vertex added to the distance lists weight at vertex u
                    ## This calculates the distances from u to each neightbour vertex essentially
                    dic = distance[u] + self.graph[u][v]
                    if dic < distance[v]:
                        ## when the shorter distance is found, we store the vertex u in the previous list and update the
                        # distance list vertex position value
                        distance[v] = dic
                        previous[v] = u


        path = []
        current = end
        while current != None:
            path.append(current)
            current = previous[current]
            #print(current)

        #print("Polku:",path)
        path.reverse()
        #print("Path:",path)

        if path[0] == end:
            return -1

        for vertex in path:
            print(vertex, end=" ")
        print()

        return

    def minVertex(self, queue, distance):
        smollest = None
        for i in queue:
            if smollest is None or distance[i] < distance[smollest]:
                smollest = i
        #         print("smollest Updated")
        # print("Smollest returned")
        return smollest

if __name__ == "__main__":

    # graph = Graph(10)
    # edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
    #          (1, 4,  3), (2, 3,  7), (2, 5, 25),
    #          (3, 4, 12), (3, 5, 15), (3, 6,  4),
    #          (3, 7, 15), (3, 8, 20), (4, 7,  2),
    #          (5, 8,  2), (6, 7,  8), (6, 8, 13),
    #          (6, 9, 15), (7, 9,  5), (8, 9,  1))
    # for u, v, w in edges:
    #     graph.add(u, v, w)
    # graph.printer()
    # graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    #graph.remove(3, 6)
    #graph.remove(5, 6)
    #graph.shortest_path(0, 9)   # 0 2 3 5 8 9


    graph = Graph(10)

    connections = ((0, 6, 15), (0, 7, 13), (1, 0, 12),
                (1, 2, 19), (2, 3, 20), (3, 6, 24),
                (4, 3, 29), (5, 4, 17), (5, 6, 14),
                (6, 1, 16), (6, 2, 22), (6, 4, 19),
                (7, 5, 29), (7, 6, 11), (7, 2, 25))

    for u, v, w in connections:
        graph.add(u, v, w)
    #
    graph.shortest_path(0, 4)
    graph.shortest_path(1, 5)
    graph.shortest_path(7, 3)
    #
    graph.remove(1, 0)
    graph.remove(7, 6)
    graph.remove(5, 4)
    graph.remove(6, 1)
    #
    # #graph.shortest_path(1, 6)
    print(graph.shortest_path(1, 5))         # should return -1
    # #graph.shortest_path(7, 3)
    # #graph.shortest_path(3, 4)
