class Graph:

    def __init__(self, n):
        self.N = n
        self.adj_matrix = [[0] * n for i in range(n)]
        self.adj_list = [[] for i in range(n)]

    def add(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
        self.adj_list[u].sort()
        self.adj_list[v].sort()

        return

    def remove(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)

        return

    def dft(self, start):
        print(start, end=" ")
        #print(self.adj_list)
        blastedThrough = [start]
        self.__dftHeeeeelp(start, blastedThrough)
        print()

    def __dftHeeeeelp(self, vertex, blastedThrough):
        for n in self.adj_list[vertex]:
            if n not in blastedThrough:
                print(n, end=" ")
                blastedThrough.append(n)
                self.__dftHeeeeelp(n, blastedThrough)

    def bft(self, start):
        visited = [False] * self.N
        queue = [start]

        visited[start] = True

        while queue:
            goneThrough = queue[0]
            print(goneThrough, end=" ")
            queue.pop(0)
            for i in range(self.N):
                if (self.adj_matrix[goneThrough][i] != 0 and not visited[i]):
                    queue.append(i)
                    visited[i] = True
        print()
        return


if __name__=="__main__":
    graph = Graph(6)


    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))

    for u, v in edges:
        graph.add(u, v)


    graph.dft(0)           # 0 2 1 5 3 4
    graph.bft(0)           # 0 2 3 4 1 5
    #
    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)           # 0 3 2 1 5 4
    graph.bft(0)           # 0 3 4 2 5 1
