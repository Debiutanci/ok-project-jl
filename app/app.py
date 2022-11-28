mapping_var = {
    0: "r",
    1: "s",
    2: "t",
    3: "x",
    4: "y",
    5: "z",
}

class Graph:
    def __init__(self, v) -> None:
        self.v = v
        self.stack = []
        self.visited = [False for _ in range(self.v + 1)]
        self.adj = [[] for _ in range(self.v + 1)]

    def insert_relation(self, vertex_id, ):
        ...


def topologicalSortUtil(v):
    global Stack, visited, adj
    visited[v] = True
    for i in adj[v]:
        if (not visited[i[0]]):
            topologicalSortUtil(i[0])
    Stack.append(v)


def longestPath(s):
    max_lens = {
        "r": [],
        "s": [],
        "t": [],
        "x": [],
        "y": [],
        "z": []
    }

    global Stack, visited, adj, V
    dist = [-10**9 for i in range(V)]
 
    for i in range(V):
        if (visited[i] == False):
            topologicalSortUtil(i)

    dist[s] = 0
    while (len(Stack) > 0):

        u = Stack[-1]
        del Stack[-1]
        current_path = [mapping_var[s]]
        if (dist[u] != -10**9):
            change = False
            for i in adj[u]:
                change = False
                if (dist[i[0]] < dist[u] + i[1]):
                    change = True
                    dist[i[0]] = dist[u] + i[1]
                    current_path.append(mapping_var[i[0]])

                if change:
                    path_before = [_ for _ in max_lens[mapping_var[u]]]
                    path_before.extend(mapping_var[u])
                    max_lens[mapping_var[i[0]]] = path_before

    response = {
        "r": {"len": dist[0], "path": max_lens["r"]},
        "s": {"len": dist[1], "path": max_lens["s"]},
        "t": {"len": dist[2], "path": max_lens["t"]},
        "x": {"len": dist[3], "path": max_lens["x"]},
        "y": {"len": dist[4], "path": max_lens["y"]},
        "z": {"len": dist[5], "path": max_lens["z"]}
    }

    for k, value in response.items():
        value["path"].append(k)

    for item in response.items():
        print(item)
    
if __name__ == '__main__':
    V, Stack, visited = 6, [], [False for i in range(7)]
    adj = [[] for i in range(7)]

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

    for arr in data:
        adj[arr[0]].append(arr[1])

    s = 0
    print("Following are longest distances from source vertex ",s)
    longestPath(s)

# ================================================================================================


def app():
    V = 6
    stack = ...
    ...
