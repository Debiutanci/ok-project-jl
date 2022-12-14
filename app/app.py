from collections import defaultdict
from graphviz import Digraph


MINUS_PATH = -10000000
PATH_KEY = "path"
LEN_KEY = "len"
METHOD_LONGEST_LONGEST = "LONGEST_LONGEST"
METHOD_ALL_LONGEST = "ALL_LONGEST"


def get_disgraph_by_data(data, mapping_var):
    d = Digraph()
    
    for k, _ in mapping_var.items():
        d.node(f"{k}", f"{k}")
    edges = []
    for arr in data:
        edges.append(f"{arr[0]}{arr[1][0]}")
    d.edges(edges)
    print(d.source)
    d.render(view=True)


class TempGraph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.all_paths = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths_util(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        if u == d:
            print(path)
            self.all_paths.append(list(path))
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.print_all_paths_util(i, d, visited, path)
        path.pop()
        visited[u]= False

    def print_all_paths(self, s, t):
        visited = [False]*(self.v)
        path = []
        self.print_all_paths_util(s, t, visited, path)
        return self.all_paths


class MainGraph:

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
        self._forced_response = None
        self.temp_graph_instance = TempGraph(v=v)
        self.data = None

    def __generate_static_temp_graph(self, data):
        for arr in data:
            self.temp_graph_instance.addEdge(
                u=arr[0],
                v=arr[1][0]
            )

    def __set_max_lens_and_mapping_var(self):
        for gk in self.gkeys:
            self.max_lens[gk] = []
        for _ in range(self.v):
            self.mapping_var[_] = self.gkeys[_]

    def create(self, data):
        self.data = data
        self.__generate_static_temp_graph(data=data)
        for arr in data:
            self.adj[arr[0]].append(arr[1])

    def topological_sort(self, v):
        self.visited[v] = True
        for i in self.adj[v]:
            if (not self.visited[i[0]]):
                self.topological_sort(i[0])
        self.stack.append(v)

    def longest_path(self, s):
        dist = [MINUS_PATH for _ in range(self.v)]

        for i in range(self.v):
            if self.visited[i] == False:
                self.topological_sort(i)

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
        for i, gk in enumerate(self.gkeys):
            response[gk] = {LEN_KEY: dist[i], PATH_KEY: self.max_lens[gk]}

        for k, value in response.items():
            value[PATH_KEY].append(k)

        self.__cached_response = response
        return response

    def display_longest_path_info(self):
        for item in self.__cached_response.items():
            print(item)

    def delete_vs(self, longest_to_forced):
        dup_data = []

        for arr in self.data:
            if arr[0] in longest_to_forced or arr[1][0] in longest_to_forced:
                pass
            else:
                dup_data.append(arr)
        return dup_data

    def _get_cached_response(self):
        return self.__cached_response

    """=============================================================="""
    def get_longest_path_from_response(self):
        max_res = -1
        res = None
        for _, row in self.__cached_response.items():
            if row[LEN_KEY] > max_res:
                res = row[PATH_KEY]
        return res

    def get_all_paths(self, s, f):
        return self.temp_graph_instance.print_all_paths(s=s, t=f)

    def __util(self, path_to_forced, f):
        smaller_graph = self.delete_vs(path_to_forced)
        inside_instance = MainGraph(self.v)
        inside_instance.create(smaller_graph)
        _ = inside_instance.longest_path(s=f)
        second_longest = inside_instance.get_longest_path_from_response()
        res = []
        res.extend(path_to_forced)
        res.extend(second_longest)
        print(res)
        self._forced_response = res
        return res

    def reverse_mapping_var(self, value):
        for k, v in self.mapping_var.items():
            if v == value:
                return k
        raise Exception("...")

    def get_len_by_path(self, path):
        reversed_path = [self.reverse_mapping_var(_) for _ in path]
        l = 0
        for rel in range(1, len(path), 1):
            source = reversed_path[rel-1]
            target = reversed_path[rel]
            for row in self.data:
                if source == row[0] and target == row[1][0]:
                    l += row[1][1]
        return l

    def get_forced_response(self, options):
        res = {}
        for i, optional_path in enumerate(options):
            res[i] = {PATH_KEY: optional_path, LEN_KEY: self.get_len_by_path(optional_path)}
        return res

    def longest_path_with_forced(self, s, f, method):
        self.longest_path(s=s)
        if method == METHOD_ALL_LONGEST:
            options = []
            for path_to_forced in self.get_all_paths(s=s, f=f):
                path_to_forced.pop()
                letters_path = [self.mapping_var[_] for _ in path_to_forced]
                options.append(self.__util(letters_path, f))
            return self.get_forced_response(options=options)

        elif method == METHOD_LONGEST_LONGEST:
            longest_to_forced = self.__cached_response[self.mapping_var[f]][PATH_KEY]
            longest_to_forced.pop()
            path = self.__util(longest_to_forced, f)
            return [path]

        else:
            raise Exception("Invalid method!")


class Configuration:
    def __init__(self, v, forced_checker, f, s, method) -> None:
        self.v = v
        self.forced_checker = forced_checker
        self.f = f
        self.s = s
        self.method = method


class Alg:
    def __init__(self, main_graph: MainGraph, configuration: Configuration) -> None:
        self.main_graph = main_graph
        self.configuration = configuration

    def execute(self):
        if not self.configuration.forced_checker:
            _ = self.main_graph.longest_path(s=self.configuration.s)
            self.main_graph.display_longest_path_info()
        else:
            res = self.main_graph.longest_path_with_forced(s=self.configuration.s, f=self.configuration.f, method=self.configuration.method)
            for obj in res.items():
                print(obj)


def app():
    v = 6
    s = 0
    f = 2 #2
    forced_checker = True
    method = "ALL_LONGEST" # "LONGEST_LONGEST" # "ALL_LONGEST"
    configuration = Configuration(v=v,forced_checker=forced_checker, f=f, s=s, method=method)
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
    graph = MainGraph(v=configuration.v)
    graph.create(data=data)

    alg = Alg(main_graph=graph, configuration=configuration)
    alg.execute()

    get_disgraph_by_data(data, graph.mapping_var)


if __name__ == '__main__':
    app()
