class Graph:

    def __init__(self, n):
        self.N = n
        self.adj_matrix = [[0] * n for i in range(n)]

    def add(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        return

    def remove(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

        return


    def __dftHeeeeelp(self, v, blastedThrough):
        blastedThrough[v] = True
        for n in range(self.N):
            if not blastedThrough[n] and self.adj_matrix[v][n] == 1:
                #print(n, end=" ")
                self.__dftHeeeeelp(n, blastedThrough)


    def subgraphs(self):
        subs = 0
        blastedThrough = [False] * self.N
        for v in range(self.N):
            if not blastedThrough[v]:
                subs += 1
                self.__dftHeeeeelp(v, blastedThrough)
        return subs

if __name__ == "__main__":
    graph = Graph(6)
    connections = ((0, 4), (2, 1),
                   (2, 5), (3, 0),
                   (5, 1))
    for u, v in connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 2

    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1
