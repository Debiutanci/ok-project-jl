MINUS_PATH = -10000000


class Graph:

    @staticmethod
    def generate_keys(quantity):
        ascii_iter = ord("a")
        gkeys = []
        for _ in range(quantity):
            gkeys.append(chr(ascii_iter))
            ascii_iter += 1
        return gkeys

    def __init__(self, v) -> None:
        self.v = v
        self.gkeys = self.generate_keys(v)
        self.stack = []
        self.visited = [False for _ in range(self.v + 1)]
        self.adj = [[] for _ in range(self.v + 1)]
        self.max_lens = {}
        self.mapping_var = {}
        self.__set_max_lens_and_mapping_var()
        self.__cached_response = None

    def __set_max_lens_and_mapping_var(self):
        for gk in self.gkeys:
            self.max_lens[gk] = []
        for _ in range(self.v):
            self.mapping_var[_] = self.gkeys[_]

    def create(self, data):
        for arr in data:
            self.adj[arr[0]].append(arr[1])

    def topologicalSortUtil(self, v):
        self.visited[v] = True
        for i in self.adj[v]:
            if (not self.visited[i[0]]):
                self.topologicalSortUtil(i[0])
        self.stack.append(v)


    def longestPath(self, s):
        dist = [MINUS_PATH for _ in range(self.v)]

        for i in range(self.v):
            if self.visited[i] == False:
                self.topologicalSortUtil(i)

        dist[s] = 0
        while (len(self.stack) > 0):
            u = self.stack[-1]
            del self.stack[-1]
            current_path = [self.mapping_var[s]]
            if (dist[u] != MINUS_PATH):
                change = False
                for i in self.adj[u]:
                    change = False
                    if (dist[i[0]] < dist[u] + i[1]):
                        change = True
                        dist[i[0]] = dist[u] + i[1]
                        current_path.append(self.mapping_var[i[0]])

                    if change:
                        path_before = [_ for _ in self.max_lens[self.mapping_var[u]]]
                        path_before.extend(self.mapping_var[u])
                        self.max_lens[self.mapping_var[i[0]]] = path_before

        response = {}
        for gk in self.gkeys:
            response[gk] = {"len": dist[0], "path": self.max_lens[gk]}

        for k, value in response.items():
            value["path"].append(k)

        self.__cached_response = response
        return response

    def display_longest_path_info(self):
        for item in self.__cached_response.items():
            print(item)


if __name__ == '__main__':
    pass

def app():
    v = 6
    data = [
        [0, [1, 5]],
        [0, [2, 3]],
        [1, [3, 6]],
        [1, [2, 2]],
        [2, [4, 4]],
        [2, [5, 2]],
        [2, [3, 7]],
        [3, [5, 1]],
        [3, [4, -1]],
        [4, [5, -2]]
    ]

    graph = Graph(v=v)
    graph.create(data=data)
    s = 0
    _ = graph.longestPath(s=s)
    graph.display_longest_path_info()
