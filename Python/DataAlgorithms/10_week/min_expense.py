class Graph:

    def __init__(self, n):
        self.N = n
        self.graph = [[0] * self.N for i in range(self.N)]
        #self.list = [[] for i range(self.N)]

    def add(self, u, v, w):
        if u >= self.N or v >= self.N:
            return
        self.graph[u][v] = w
        self.graph[v][u] = w

        #self.list[u].append((v,w))

    def remove(self, u, v):
        #if u >= self.N or v >= self.N:
        #    return
        self.graph[u][v] = 0
        self.graph[v][u] = 0
        #if v in self.list[u]:
            #self.list[u].remove()
    #
    def printer(self):
        for i in range(self.N):
            for j in range(self.N):
                print(f"{self.graph[i][j]:3d}", end="")
            print()


    def min_expense(self):
        #print("Holly", self.N)
        #self.printer()
        distance = [float('inf')] * self.N
        #previous = [None] * self.N
        queue = [i for i in range(self.N)]

        distance[0] = 0

        while queue:
            u = self.minVertex(queue, distance)
            #print(u)
            # Vertex with shortest distance remaining in queue is removed from queue
            queue.remove(u)

            for v in range(self.N):
                ## this checks that there indeed is an edge between vertices u and v
                if self.graph[u][v] != 0 and v in queue:

                    # Distance (weight) from current u vertex to v vertex added to the distance lists weight at vertex u
                    ## This calculates the distances from u to each neightbour vertex essentially
                    dic = self.graph[u][v] # distance[u] +
                    if dic < distance[v]:
                        ## when the shorter distance is found, we store the vertex u in the previous list and update the
                        # distance list vertex position value
                        distance[v] = dic
                        #previous[v] = u


        total = 0
        for num in distance:
            if num != float('inf'):
               # print(num)
                total += num

        return total

    def shortest_path(self, start, end):
        distance = [float('inf')] * self.N
        previous = [None] * self.N
        queue = [i for i in range(self.N)]

        distance[start] = 0

        while queue:
            u = self.minVertex(queue, distance)
            #print(u)

            queue.remove(u)

            for v in range(self.N):
                if self.graph[u][v] != 0:
                    dic = distance[u] + self.graph[u][v]
                    if dic < distance[v]:
                        distance[v] = dic
                        previous[v] = u

        path = []
        current = end
        while current != None:
            path.append(current)
            current = previous[current]
        path.reverse()
        if len(path) <= 1:
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
    graph = Graph(6)
    connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.min_expense())  # 15

    graph.remove(2, 3)

    print(graph.min_expense())  # 16

