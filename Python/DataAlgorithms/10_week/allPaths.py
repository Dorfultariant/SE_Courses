class Graph:

    def __init__(self, n):
        self.N = n
        self.graph = [[0] * self.N for i in range(self.N)]
        self.short = [[]]

    def nuller(self, matrix):
        matrix = [[-1] * self.N for i in range(self.N)]
        for i in range(self.N):
            matrix[i][i] = 0
        return matrix

    def add(self, u, v, w):
        if u >= self.N or v >= self.N:
            return
        self.graph[u][v] = w
        #self.list[u].append((v,w))

    def remove(self, u, v):
        if u >= self.N or v >= self.N:
            return
        self.graph[u][v] = 0
        #if v in self.list[u]:
            #self.list[u].remove()

    def printer(self, matrix):
        for i in range(self.N):
            for j in range(self.N):
                if matrix[i][j] == float("inf"):
                    print(f"{0:3d}", end="")
                    continue
                print(f"{matrix[i][j]:3d}", end="")
            print()


    def all_paths(self):
        self.short = self.nuller(self.short)
        for i in range(self.N):  # Initialize D with weights
            for j in range(self.N):
                if self.graph[i][j] != 0:
                    self.short[i][j] = self.graph[i][j]

        for k in range(self.N):  # Compute all k paths
            for i in range(self.N):
                for j in range(self.N):
                    if (self.short[i][k] != -1 and
                        self.short[k][j] != -1 and
                        self.short[i][j] > self.short[i][k] + self.short[k][j]):
                        # Executed
                        self.short[i][j] = self.short[i][k] + self.short[k][j]
        for u in range(self.N):
            for v in range(self.N):
                dist = self.dijkstra(u, v)
                if dist > 0:
                    self.short[u][v] = dist
        for u in range(self.N):
            for v in range(self.N):
                if self.short[u][v] == float("inf"):
                    self.short[u][v] = -1


        return self.short


    def dijkstra(self, start, end):
        distance = [float("inf")] * self.N
        #previous = [None] * self.N
        queue = [i for i in range(self.N)]

        distance[start] = 0

        while queue:
            u = self.minVertex(queue, distance)
            #print(u)
            # Vertex with shortest distance remaining in queue is removed from queue
            queue.remove(u)

            for v in range(self.N):
                ## this checks that there indeed is an edge between vertices u and v
                if self.graph[u][v] != 0: #  and v in queue

                    # Distance (weight) from current u vertex to v vertex added to the distance lists weight at vertex u
                    ## This calculates the distances from u to each neightbour vertex essentially
                    dic = distance[u] + self.graph[u][v] #
                    if dic < distance[v] : #and distance[v] != -2
                        ## when the shorter distance is found, we store the vertex u in the previous list and update the
                        # distance list vertex position value
                        distance[v] = dic
                        #previous[v] = u
        #print(distance[end])
        return distance[end]

    def minVertex(self, queue, distance):
        smollest = None
        for i in queue:
            if smollest is None or distance[i] < distance[smollest] :#and distance[i] != -2
                smollest = i
        #         print("smollest Updated")
        # print("Smollest returned")
        return smollest

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()

    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    #  0 12  7  8  9  9
    # -1  0 -1 -1 -1 -1
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    # -1  7 -1 -1  0  1
    # -1  6 -1 -1 -1  0
